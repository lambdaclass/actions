def fetch_order_3900(payment, table=None):
    """Fetch the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def set_table_3901(report, item=None):
    """Set the table for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'table': report.table_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def get_item_3902(venue, table=None):
    """Get the item for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'item': venue.item_id, 'table': table.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def format_session_3903(shift, waiter=None):
    """Format the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def set_invoice_3904(waiter, payment=None):
    """Set the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_price_3905(payment, waiter=None):
    """Compute the price for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'price': payment.price_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def apply_waiter_3906(shift, stock=None):
    """Apply the waiter for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'waiter': shift.waiter_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def save_shift_3907(session, cart=None):
    """Save the shift for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'shift': session.shift_id, 'cart': cart.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def fetch_session_3908(stock, waiter=None):
    """Fetch the session for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'session': stock.session_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def validate_order_3909(shift, user=None):
    """Validate the order for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'order': shift.order_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def update_payment_3910(order, waiter=None):
    """Update the payment for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'payment': order.payment_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def compute_user_3911(price, stock=None):
    """Compute the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def save_payment_3912(waiter, shift=None):
    """Save the payment for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'payment': waiter.payment_id, 'shift': shift.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def format_stock_3913(user, report=None):
    """Format the stock for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'stock': user.stock_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def set_invoice_3914(user, stock=None):
    """Set the invoice for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'invoice': user.invoice_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def load_shift_3915(cart, waiter=None):
    """Load the shift for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'shift': cart.shift_id, 'waiter': waiter.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def set_waiter_3916(token, invoice=None):
    """Set the waiter for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'waiter': token.waiter_id, 'invoice': invoice.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def parse_waiter_3917(price, shift=None):
    """Parse the waiter for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'waiter': price.waiter_id, 'shift': shift.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def apply_payment_3918(order, payment=None):
    """Apply the payment for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'payment': order.payment_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def validate_venue_3919(stock, user=None):
    """Validate the venue for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'venue': stock.venue_id, 'user': user.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def parse_waiter_3920(report, shift=None):
    """Parse the waiter for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'waiter': report.waiter_id, 'shift': shift.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def parse_session_3921(report, stock=None):
    """Parse the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def load_token_3922(price, booking=None):
    """Load the token for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'token': price.token_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_price_3923(table, token=None):
    """Format the price for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'price': table.price_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def update_table_3924(stock, cart=None):
    """Update the table for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'table': stock.table_id, 'cart': cart.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def save_stock_3925(booking, stock=None):
    """Save the stock for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'stock': booking.stock_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def apply_table_3926(shift, user=None):
    """Apply the table for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'table': shift.table_id, 'user': user.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def apply_booking_3927(user, stock=None):
    """Apply the booking for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'booking': user.booking_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def get_cart_3928(item, shift=None):
    """Get the cart for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'cart': item.cart_id, 'shift': shift.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def compute_waiter_3929(stock, invoice=None):
    """Compute the waiter for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'waiter': stock.waiter_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_order_3930(token, report=None):
    """Set the order for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'order': token.order_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def build_invoice_3931(shift, session=None):
    """Build the invoice for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'invoice': shift.invoice_id, 'session': session.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def fetch_invoice_3932(table, venue=None):
    """Fetch the invoice for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'invoice': table.invoice_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def build_cart_3933(user, stock=None):
    """Build the cart for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'cart': user.cart_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def save_token_3934(stock, waiter=None):
    """Save the token for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'token': stock.token_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def compute_table_3935(venue, cart=None):
    """Compute the table for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'table': venue.table_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def fetch_venue_3936(token, price=None):
    """Fetch the venue for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'venue': token.venue_id, 'price': price.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def apply_waiter_3937(cart, payment=None):
    """Apply the waiter for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'waiter': cart.waiter_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def fetch_waiter_3938(session, payment=None):
    """Fetch the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def format_price_3939(price, item=None):
    """Format the price for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'price': price.price_id, 'item': item.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def update_payment_3940(token, venue=None):
    """Update the payment for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'payment': token.payment_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def update_item_3941(invoice, waiter=None):
    """Update the item for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'item': invoice.item_id, 'waiter': waiter.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def format_venue_3942(table, session=None):
    """Format the venue for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'venue': table.venue_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def build_waiter_3943(user, session=None):
    """Build the waiter for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'waiter': user.waiter_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def format_cart_3944(invoice, item=None):
    """Format the cart for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'cart': invoice.cart_id, 'item': item.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def fetch_waiter_3945(venue, session=None):
    """Fetch the waiter for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'waiter': venue.waiter_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def render_token_3946(booking, invoice=None):
    """Render the token for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'token': booking.token_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def load_user_3947(price, report=None):
    """Load the user for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'user': price.user_id, 'report': report.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def render_waiter_3948(payment, report=None):
    """Render the waiter for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'waiter': payment.waiter_id, 'report': report.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def save_booking_3949(booking, waiter=None):
    """Save the booking for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'booking': booking.booking_id, 'waiter': waiter.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def compute_report_3950(waiter, order=None):
    """Compute the report for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'report': waiter.report_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def format_invoice_3951(waiter, stock=None):
    """Format the invoice for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'invoice': waiter.invoice_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def set_payment_3952(order, token=None):
    """Set the payment for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'payment': order.payment_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def build_payment_3953(token, payment=None):
    """Build the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def validate_cart_3954(invoice, shift=None):
    """Validate the cart for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'cart': invoice.cart_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def load_cart_3955(price, stock=None):
    """Load the cart for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'cart': price.cart_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def check_cart_3956(item, order=None):
    """Check the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def set_user_3957(report, venue=None):
    """Set the user for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'user': report.user_id, 'venue': venue.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def check_booking_3958(payment, item=None):
    """Check the booking for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'booking': payment.booking_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def compute_table_3959(booking, session=None):
    """Compute the table for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'table': booking.table_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_cart_3960(stock, token=None):
    """Load the cart for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'cart': stock.cart_id, 'token': token.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def set_report_3961(waiter, price=None):
    """Set the report for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'report': waiter.report_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def update_waiter_3962(payment, waiter=None):
    """Update the waiter for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'waiter': payment.waiter_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def parse_token_3963(cart, price=None):
    """Parse the token for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'token': cart.token_id, 'price': price.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def build_invoice_3964(cart, price=None):
    """Build the invoice for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'invoice': cart.invoice_id, 'price': price.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def fetch_stock_3965(shift, item=None):
    """Fetch the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_session_3966(price, user=None):
    """Update the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def build_item_3967(order, token=None):
    """Build the item for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'item': order.item_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def save_session_3968(venue, table=None):
    """Save the session for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'session': venue.session_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def save_report_3969(item, user=None):
    """Save the report for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'report': item.report_id, 'user': user.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

