from odoo import api, fields, models

class BankAccount(models.Model):
    _name = 'bank.account'
    _description = 'Bank Account'

    name = fields.Char(string='Account Name')
    description = fields.Char(string='Description')
    payment_gateway = fields.Char(string='Payment Gateway')
    account_no = fields.Char(string='Account No')
    ifsc_code = fields.Char(string='IFSC Code')
    bank_name = fields.Char(string='Bank Name')
    branch = fields.Char(string='Branch')


class FeeCategory(models.Model):
    _name = 'fee.category'
    _description = 'Fee Category'

    name = fields.Char(string='Category Name')
    code = fields.Char(string='Code')
    category_type = fields.Selection([
        ('fixed', 'Fixed'),
        ('flexi', 'Flexi'),
        ('fixed_flexi', 'Fixed & Flexi')
    ], string='Category Type')
    bank_account = fields.Many2one('bank.account', string='Bank Account')
    incharge = fields.Many2one('res.users', string='Incharge')

    @api.onchange('name', 'category_type')
    def _compute_fee_group_name(self):
        for record in self:
            record.fee_group_name = record.name


class UseCaseConfiguringBankAndFee(models.Model):
    _name = 'usecase.configuring.bank.fee'
    _description = 'Use Case: Configuring Bank Accounts and Fee Categories for Students'

    name = fields.Char(string='Use Case Name', default='Configuring Bank Accounts and Fee Categories for Students')
    actors = fields.Text(string='Actors', default='Accountant, Office Admin')
    description = fields.Text(string='Description', default='This use case describes the process of configuring bank accounts and fee categories for students in the system.')
    preconditions = fields.Text(string='Preconditions', default='The user has appropriate permissions and access rights as an Accountant or Office Admin.')
    flow_of_events = fields.Text(string='Flow of Events', default='1. Configuring Bank Accounts for Students:\n\nThe Accountant/Office Admin selects the "Configuration" main menu.\nFrom the submenu, the user selects "Bank Account" to configure bank accounts for students.\nThe system displays the Bank Account form view with the following fields: Account Name, Description, Payment Gateway, Account No, IFSC Code, Bank Name, and Branch.\nThe user enters the required information in each field:\nAccount Name: [Text input]\nDescription: [Text input]\nPayment Gateway: [Text input]\nAccount No: [Text input]\nIFSC Code: [Text input]\nBank Name: [Text input]\nBranch: [Text input]\nThe user saves the bank account details.\nThe system stores the bank account information in the database.\n\n2. Configuring Fee Categories for Students:\n\nThe Accountant/Office Admin selects the "Configuration" main menu.\nFrom the submenu, the user selects "Fee Categories" to configure fee categories for students.\nThe system displays the Fee Category form view with the following fields: Category Name, Code, Category Type, Bank Account, and Incharge.\nThe user enters the required information in each field:\nCategory Name: [Text input]\nCode: [Text input]\nCategory Type: [Radio button selection: Fixed/Flexi/Fixed & Flexi]\nBank Account: [List box selection]\nIncharge: [List box selection]\nThe user saves the fee category details.\nThe system stores the fee category information in the database.\nThe system displays the "Fee Group" tab under the Fee Category, automatically capturing and displaying the name.')
    postconditions = fields.Text(string='Postconditions', default='Bank accounts and fee categories for students are successfully configured and stored in the system.')
    exceptions = fields.Text(string='Exceptions', default='If any required fields are not filled or contain invalid data, an error message is displayed, prompting the user to correct the information.\nIf there are any technical issues or errors during the saving process, an error message is displayed, and the user is advised to try again later.')


class Task(models.Model):
    _name = 'task'
    _description = 'Task'

    name = fields.Char(string='Task Name')
    description = fields.Text(string='Description')
    user_story_id = fields.Many2one('user.story', string='User Story')


class UserStory(models.Model):
    _name = 'user.story'
    _description = 'User Story'

    name = fields.Char(string='User Story')
    acceptance_criteria = fields.Text(string='Acceptance Criteria')


class UserStoryConfiguringBankAccounts(models.Model):
    _name = 'user.story.configuring.bank.accounts'
    _description = 'User Story: Configuring Bank Accounts for Students'

    name = fields.Char(string='User Story', default='Configuring Bank Accounts for Students')
    acceptance_criteria = fields.Text(string='Acceptance Criteria', default='1. Given that I am logged in as an Accountant or Office Admin, I should have access to the bank account configuration feature.\n2. When I navigate to the bank account configuration page, I should be able to enter the bank account details including Account Name, Description, Payment Gateway, Account No, IFSC Code, Bank Name, and Branch.\n3. After entering the details, I should be able to save the bank account information and have it stored in the database.')


class UserStoryConfiguringFeeCategories(models.Model):
    _name = 'user.story.configuring.fee.categories'
    _description = 'User Story: Configuring Fee Categories for Students'

    name = fields.Char(string='User Story', default='Configuring Fee Categories for Students')
    acceptance_criteria = fields.Text(string='Acceptance Criteria', default='1. Given that I am logged in as an Accountant or Office Admin, I should have access to the fee category configuration feature.\n2. When I navigate to the fee category configuration page, I should be able to enter the fee category details including Category Name, Code, Category Type, Bank Account, and Incharge.\n3. After entering the details, I should be able to save the fee category information and have it stored in the database.\n4. The system should automatically display the Name field under the "Fee Group" tab based on the selected fee category fields.')


class UserStoryConfiguringBankAndFee(models.Model):
    _name = 'user.story.configuring.bank.fee'
    _description = 'User Story: Configuring Bank Accounts and Fee Categories for Students'

    name = fields.Char(string='User Story', default='Configuring Bank Accounts and Fee Categories for Students')
    acceptance_criteria = fields.Text(string='Acceptance Criteria', default='1. Given that I am logged in as an Accountant or Office Admin, I should have access to the bank account and fee category configuration features.\n2. When I navigate to the bank account configuration page, I should be able to enter the bank account details including Account Name, Description, Payment Gateway, Account No, IFSC Code, Bank Name, and Branch.\n3. After entering the details, I should be able to save the bank account information and have it stored in the database.\n4. When I navigate to the fee category configuration page, I should be able to enter the fee category details including Category Name, Code, Category Type, Bank Account, and Incharge.\n5. After entering the details, I should be able to save the fee category information and have it stored in the database.\n6. The system should automatically display the Name field under the "Fee Group" tab based on the selected fee category fields.')
