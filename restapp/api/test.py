import stripe

STRIPE_CLIENT_SECRET_CONNECT = 'sk_test_51HOf1xFRWUoNfXLcIt1xQ6E3nJTwVFOIKJkorKVxrcQBqeLeuejZUdzFD4eYiT2iTiauETSYOudSqhko8HjmmWl50085B614cP'
card_token = 'tok_1HhsIUFRWUoNfXLcWjd1oIdB'
customer_id = 'cus_IITGrnFaZ7p7HA'


def create_charge(customer_id):
    stripe.api_key = STRIPE_CLIENT_SECRET_CONNECT
    charge = stripe.Charge.create(
        amount=10 * 100,
        currency='usd',
        customer=customer_id,
        description='test',
        metadata={},
    )
    print(f'charge: {charge}')


def create_token():
    stripe.api_key = STRIPE_CLIENT_SECRET_CONNECT
    token = stripe.Token.create(
        card={
            "number": "4242424242424242",
            "exp_month": 10,
            "exp_year": 2021,
            "cvc": "314",
        },
    )
    print(f'token: {token}')


def create_customer():
    stripe.api_key = STRIPE_CLIENT_SECRET_CONNECT
    customer = stripe.Customer.create(
        source='tok_1HhsIUFRWUoNfXLcWjd1oIdB',
        description="Amit Jamwal",
        email='amitjamwal85@gmail.com',
    )
    print(f'customer: {customer}')


#####################################################################################################

# create_token()

# create_customer()
create_charge(customer_id)