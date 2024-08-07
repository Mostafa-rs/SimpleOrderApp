"""
Messages
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""


class Message:
    # auth
    ERR_USER_NOT_FOUND = 'Username or password is wrong.'
    ERR_SPAM_AUTH_REQUEST = 'Too many tries. please try again later.'
    ER_REFRESH_TOKEN_REQUIRED = 'Refresh token is required.'
    ERR_REFRESH_TOKEN_INVALID = 'Refresh token is invalid.'

    # General
    ERR_TRY = 'An unexpected error occurred. please try again.'

    # Order
    ERR_ORDER_NOT_FOUND = 'Order not found.'
    ERR_ORDER_MORE_THAN_STOCK = 'You cant order more than stock.'

