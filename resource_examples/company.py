import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        COMPANY 
    RESOURCE EXAMPLE

'''

##
## GET 
##
results = dtl.companies.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.companies.get("<access_token>", "<companyId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlCompanyCreateModel("Company Name") # required param
create_model.website = ""
create_model.location = ""
create_model.industry = ""

results = dtl.companies.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlCompanyPatchModel()
patch_model.company_name = ""
patch_model.website = ""
patch_model.location = ""
patch_model.industry = ""

results = dtl.companies.patch("<access_token>", "<companyId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.companies.delete("<access_token>", "<companyId>")
print(results.status_code) # 204 for successful request