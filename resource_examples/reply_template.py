import dtleads_api_helper

dtl = dtleads_api_helper.DanielTimothyLeads() # create instance of DTLeads helper
dtl_models = dtleads_api_helper.dtl_models # get models from import

'''

     REPLY TEMPLATE 
    RESOURCE EXAMPLE

'''
##
## GET
##
results = dtl.reply_templates.get("<access_token>") # get all
details = dtl.handle_response(results)
print(details)


results = dtl.reply_templates.get("<access_token>", "<replyTemplateId>") # get by Id
details = dtl.handle_response(results)
print(details)


##
## CREATE
##
create_model = dtl_models.DtlReplyTemplateCreateModel("Reply Template Name", "<p>reply template HTML body</p>") # required params

results = dtl.reply_templates.create("<access_token>", create_model.get_json_object())
details = dtl.handle_response(results)
print(details)


##
## UPDATE
##
patch_model = dtl_models.DtlReplyTemplatePatchModel()
patch_model.name = "patch reply name"
patch_model.html_body = "<p>patch reply body</p>"

results = dtl.reply_templates.patch("<access_token>", "<replyTemplateId>", patch_model.get_json_object())
details = dtl.handle_response(results)
print(details)

##
## DELETE
##
results = dtl.reply_templates.delete("<access_token>", "<replyTemplateId>")
print(results.status_code) # 204 for successful request
