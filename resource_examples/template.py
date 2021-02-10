import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

        TEMPLATE 
    RESOURCE EXAMPLE

'''

##
## GET
##
results = dtl.templates.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)

results = dtl.templates.get("<access_token>", "<templateId>") # get by id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlTemplateCreateModel("Template Name", "Subject Line", "<p>template HTML body</p>") # required params
create_model.unsubscribe_option = True # True/False (default = True)
create_model.template_setting_id = "<templateSettingId>"

results = dtl.templates.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlTemplatePatchModel()
patch_model.name = ""
patch_model.subject = ""
patch_model.html_body = ""
patch_model.unsubscribe_option = False
patch_model.template_setting_id = ""

results = dtl.templates.patch("<access_token>", "<templateId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## DELETE
##
change_template_id = "<templateId>" # different template to change any campaigns current template when deleting
results = dtl.templates.delete("<access_token>", "<templateId>", change_template_id)
print(results.status_code) # 204 for successful request


##
## ADD REPLY TEMPLATE
##
add_reply_model = dtl_models.DtlAddReplyTemplateModel("<replyTemplateId>")
add_reply_model.schedule_time = 4320 # 3 days in minutes

results = dtl.templates.add_reply("<access_token>", "<templateId>", add_reply_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## REMOVE REPLY TEMPLATE
##
results = dtl.templates.remove_reply("<access_token>", "<templateId>", "<replyTemplateId>")
print(results.status_code) # 204 for successful request
