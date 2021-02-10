import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        ACCOUNT
    RESOURCE EXAMPLE

'''

## GET
results = dtl.account.get("<access_token>")
details = dtl.handle_response(results)
print(details)

## UPDATE
account_model = dtl_models.DtlAccountPatchModel()
account_model.company_name = ""
account_model.phone_number = ""

results = dtl.account.patch("<access_token>", account_model.get_json_object())
details = dtl.handle_response(results)
print(details)