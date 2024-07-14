class Industry:
    RESTAURANTS = 'restaurants'
    STORES = 'stores'
    WHOLESALE = 'wholesale'
    SERVICES = 'services'

    @staticmethod
    def list():
        return [Industry.RESTAURANTS, Industry.STORES, Industry.WHOLESALE, Industry.SERVICES]

class WorkflowStage:
    NEW = 'New'
    MARKET_APPROVED = 'Market Approved'
    MARKET_DECLINED = 'Market Declined'
    SALES_APPROVED = 'Sales Approved'
    WON = 'Won'
    LOST = 'Lost'

businesses = {}
