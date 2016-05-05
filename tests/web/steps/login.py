from behave import given, when, then
from tests.pageobjects.login import LoginPageObject
from nose.tools import assert_in, assert_equal, assert_true, assert_false

@given('goto page')
def step_impl(context):
    context.current_page = LoginPageObject()
    context.current_page.open().waitToDrawSection().setElements()

@given  ('select language "{langugeId}"')
def step_impl(context, langugeId):
    context.current_page.setLanguage(langugeId);

@when('set "{property}" to "{value}"')
def step_impl(context, property, value):
    a = getattr(context.current_page, property);
    #a.clear();
    a.text = value;

@when('clear input "{inputname}"')
def step_impl(context, inputname):
    getattr(context.current_page, inputname).clear();

@when('login')
def step_impl(context):
    context.current_page.loginBtn.click();
    context.current_page.loginBtn.click();

@then('Show Message "{message}"')
def step_impl(context, message):
    realMessage = context.current_page.getMessage();
    assert_equal(realMessage, message);

@then('Open main section of App')
def step_impl(context):
    context.current_page.getContentSection().wait_until_visible();

@then('flash App is loaded')
def step_impl(context):
    context.current_page.getApp().wait_until_visible();
    realUserdata = context.current_page.getApp();

@when('select choice "{portal}"')
def step_impl(context, portal):
    context.current_page.portal.click();
    if portal == 'vcd' :
        context.current_page.vcd.click();
    else:
        context.current_page.vra.click();

@then('userdata in header is equal to "{userdata}"')
def step_impl(context, userdata):
    realUserdata = context.current_page.getUserName().text;
    assert_equal(realUserdata, userdata);
