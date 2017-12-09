import time

from behave import *
from selenium.webdriver.common.action_chains import ActionChains

use_step_matcher("re")


@given("inicio sesión con las credenciales (?P<email>.+) y (?P<password>.+)")
def step_impl(context, email, password):
    email_box = element_by_id(context.driver, 'email')
    email_box.send_keys(email)

    passw = element_by_id(context.driver, 'pass')
    passw.send_keys(password)

    login = element_by_css_selector(context.driver, 'input[value="Log In"]')
    login.click()

    user_box = element_by_xpath(context.driver, '//*[@id="u_0_a"]')


@step("ingreso a la url de perfil de un amigo: (?P<friend_url>.+)")
def step_impl(context, friend_url):
    context.driver.get(friend_url)


@when("selecciono la opción para enviar mensaje")
def step_impl(context):
    msg_box = element_by_xpath(context.driver, '//*[@id="u_0_1d"]')
    msg_box.click()


@step("envío el mensaje (?P<message>.+)")
def step_impl(context, message):
    for i in range(5):
        actions = ActionChains(context.driver)
        actions.send_keys(message)
        # actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.3)


@then("el mensaje es mostrado en la ventana de chat")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


def element_by_css_selector(root, css_selector):
    try:
        return root.find_element_by_css_selector(css_selector)
    except:
        assert False, no_encontrado('css_selector', css_selector)


def elements_by_css_selector(root, css_selector):
    try:
        return root.find_elements_by_css_selector(css_selector)
    except:
        assert False, no_encontrados('css_selector', css_selector)


def element_by_id(root, id):
    try:
        return root.find_element_by_id(id)
    except:
        assert False, no_encontrado('id', id)


def element_by_xpath(root, xpath):
    try:
        return root.find_element_by_xpath(xpath)
    except:
        assert False, no_encontrado('xpath', xpath)


def elements_by_tag_name(root, tag_name):
    try:
        return root.find_elements_by_tag_name(tag_name)
    except:
        assert False, no_encontrados('tag_name', tag_name)


def no_encontrado(parametro, valor):
    return 'No se encontró el elemento con %s="%s"' % (parametro, valor)


def no_encontrados(parametro, valor):
    return 'No se encontrarion elementos con %s="%s"' % (parametro, valor)
