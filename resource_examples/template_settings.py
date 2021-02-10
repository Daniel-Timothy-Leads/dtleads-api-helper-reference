import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

    TEMPLATE SETTINGS 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.template_settings.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.template_settings.get("<access_token>", "<templateSettingId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlTemplateSettingsCreateModel("Setting Name", 2880) # 2 days (required params)
create_model.restriction_id = "<restrctionId>"

results = dtl.template_settings.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPATE
##
patch_model = dtl_models.DtlTemplateSettingsPatchModel()
patch_model.setting_name = "setting name"
patch_model.schedule_time = 4320 # 3 days

results = dtl.template_settings.patch("<access_token>", "<templateSettingId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
results = dtl.template_settings.delete("<access_token>", "<templateSettingId>")
print(results.status_code) # 204 for successful request