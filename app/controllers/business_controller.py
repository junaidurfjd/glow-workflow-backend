from ..models import businesses, WorkflowStage, Industry
from ..utils.exceptions import NotFoundException, BadRequestException
from ..utils.docorators import business_exists

class BusinessController:
    @staticmethod
    def get_next_step_info(current_stage):
        if current_stage == WorkflowStage.NEW:
            return "Provide 'industry' to progress. Only 'restaurants' and 'stores' are accepted."
        elif current_stage == WorkflowStage.MARKET_APPROVED:
            return "Provide 'contact' information to progress."
        elif current_stage == WorkflowStage.SALES_APPROVED:
            return "Set 'workflow_stage' to 'Won' or 'Lost' to progress."
        else:
            return "No further steps required."

    @staticmethod
    def create_business(data):
        fein = data.get('fein')
        if fein in businesses:
            raise BadRequestException('Business with this FEIN already exists')
        businesses[fein] = data
        businesses[fein]['workflow_stage'] = WorkflowStage.NEW
        businesses[fein]['next_step_info'] = BusinessController.get_next_step_info(WorkflowStage.NEW)

        return businesses[fein]

    @staticmethod
    @business_exists
    def approve_market(fein, data):

        business = businesses[fein]

        if business['workflow_stage'] != WorkflowStage.NEW:
            raise BadRequestException('Can only approve market for NEW businesses')

        if 'industry' not in data or data['industry'] not in Industry.list():
            raise BadRequestException(f'Invalid or missing industry. Valid values are: {Industry.list()}')

        business['industry'] = data['industry']
        if data['industry'] in [Industry.RESTAURANTS, Industry.STORES]:
            business['workflow_stage'] = WorkflowStage.MARKET_APPROVED
        else:
            business['workflow_stage'] = WorkflowStage.MARKET_DECLINED

        business['next_step_info'] = BusinessController.get_next_step_info(business['workflow_stage'])
        businesses[fein] = business
        return business
    
    @staticmethod
    @business_exists
    def approve_sales(fein, data):
        business = businesses[fein]

        if business['workflow_stage'] != WorkflowStage.MARKET_APPROVED:
            raise BadRequestException('Can only approve sales for MARKET APPROVED businesses')

        if 'contact' not in data or not isinstance(data['contact'], dict):
            raise BadRequestException('Invalid or missing contact information. Expected format: {"contact": {"name": "John Doe", "phone": "555-555-5555"}}')
        
        contact = data['contact']
        if 'name' not in contact or not isinstance(contact['name'], str):
            raise BadRequestException('Invalid or missing contact name')
        if 'phone' not in contact or not isinstance(contact['phone'], str):
            raise BadRequestException('Invalid or missing contact phone')

        business['contact'] = contact
        business['workflow_stage'] = WorkflowStage.SALES_APPROVED

        business['next_step_info'] = BusinessController.get_next_step_info(business['workflow_stage'])
        businesses[fein] = business
        return business

    @staticmethod
    @business_exists
    def set_won(fein):
        business = businesses[fein]

        if business['workflow_stage'] != WorkflowStage.SALES_APPROVED:
            raise BadRequestException('Can only set to WON for SALES APPROVED businesses')

        business['workflow_stage'] = WorkflowStage.WON
        business['next_step_info'] = BusinessController.get_next_step_info(business['workflow_stage'])
        businesses[fein] = business
        return business

    @staticmethod
    @business_exists
    def set_lost(fein):

        business = businesses[fein]

        if business['workflow_stage'] != WorkflowStage.SALES_APPROVED:
            raise BadRequestException('Can only set to LOST for SALES APPROVED businesses')

        business['workflow_stage'] = WorkflowStage.LOST
        business['next_step_info'] = BusinessController.get_next_step_info(business['workflow_stage'])
        businesses[fein] = business
        return business
    

    @staticmethod
    @business_exists
    def get_business(fein):
        business = businesses[fein]
        business['next_step_info'] = BusinessController.get_next_step_info(business['workflow_stage'])
        return business

    