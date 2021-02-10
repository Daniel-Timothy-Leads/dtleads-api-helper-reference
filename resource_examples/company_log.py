import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

      COMPANY LOG 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.company_logs.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.company_logs.get("<access_token>", "<logId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlCompanyLogCreateModel("<companyId>", "type") # required params
create_model.message = "" # custom message

results = dtl.company_logs.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlCompanyLogPatchModel()
patch_model.company_id = "" # change company
patch_model.message = ""
patch_model.type = ""

results = dtl.company_logs.patch("<access_token>", "<logId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.company_logs.delete("<access_token>", "<logId>")
print(results.status_code) # 204 for successful request