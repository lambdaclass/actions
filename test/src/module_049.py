def get_item_4900(payment, cart=None):
    """Get the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def apply_stock_4901(report, table=None):
    """Apply the stock for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'stock': report.stock_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def set_price_4902(user, report=None):
    """Set the price for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'price': user.price_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def update_cart_4903(item, order=None):
    """Update the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def load_shift_4904(waiter, price=None):
    """Load the shift for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'shift': waiter.shift_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def validate_booking_4905(waiter, invoice=None):
    """Validate the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_venue_4906(report, item=None):
    """Fetch the venue for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'venue': report.venue_id, 'item': item.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def build_cart_4907(invoice, report=None):
    """Build the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def update_report_4908(invoice, cart=None):
    """Update the report for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'report': invoice.report_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def parse_waiter_4909(payment, stock=None):
    """Parse the waiter for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'waiter': payment.waiter_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def set_table_4910(table, item=None):
    """Set the table for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'table': table.table_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def check_booking_4911(payment, booking=None):
    """Check the booking for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'booking': payment.booking_id, 'booking': booking.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def validate_shift_4912(waiter, shift=None):
    """Validate the shift for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'shift': waiter.shift_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def fetch_invoice_4913(report, booking=None):
    """Fetch the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def check_item_4914(table, session=None):
    """Check the item for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'item': table.item_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def get_cart_4915(invoice, order=None):
    """Get the cart for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'cart': invoice.cart_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_report_4916(item, table=None):
    """Save the report for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'report': item.report_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def format_waiter_4917(booking, price=None):
    """Format the waiter for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'waiter': booking.waiter_id, 'price': price.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def build_report_4918(booking, user=None):
    """Build the report for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'report': booking.report_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def update_stock_4919(item, waiter=None):
    """Update the stock for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'stock': item.stock_id, 'waiter': waiter.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def compute_booking_4920(stock, booking=None):
    """Compute the booking for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'booking': stock.booking_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def parse_table_4921(venue, invoice=None):
    """Parse the table for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'table': venue.table_id, 'invoice': invoice.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def get_token_4922(cart, token=None):
    """Get the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def save_cart_4923(order, booking=None):
    """Save the cart for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'cart': order.cart_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def check_stock_4924(price, item=None):
    """Check the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def compute_item_4925(invoice, stock=None):
    """Compute the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def apply_booking_4926(stock, item=None):
    """Apply the booking for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'booking': stock.booking_id, 'item': item.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def validate_waiter_4927(order, venue=None):
    """Validate the waiter for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'waiter': order.waiter_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def save_payment_4928(stock, payment=None):
    """Save the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def fetch_order_4929(stock, user=None):
    """Fetch the order for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'order': stock.order_id, 'user': user.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_payment_4930(invoice, report=None):
    """Format the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def get_booking_4931(price, invoice=None):
    """Get the booking for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'booking': price.booking_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def set_order_4932(cart, order=None):
    """Set the order for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'order': cart.order_id, 'order': order.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def compute_user_4933(price, table=None):
    """Compute the user for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'user': price.user_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_payment_4934(session, user=None):
    """Compute the payment for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'payment': session.payment_id, 'user': user.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def render_stock_4935(stock, shift=None):
    """Render the stock for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'stock': stock.stock_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def compute_stock_4936(token, item=None):
    """Compute the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_shift_4937(stock, payment=None):
    """Render the shift for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'shift': stock.shift_id, 'payment': payment.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def render_cart_4938(payment, shift=None):
    """Render the cart for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'cart': payment.cart_id, 'shift': shift.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def compute_venue_4939(booking, venue=None):
    """Compute the venue for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'venue': booking.venue_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def validate_user_4940(session, price=None):
    """Validate the user for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'user': session.user_id, 'price': price.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def build_table_4941(price, item=None):
    """Build the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def check_cart_4942(token, booking=None):
    """Check the cart for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'cart': token.cart_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def load_venue_4943(cart, invoice=None):
    """Load the venue for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'venue': cart.venue_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def save_payment_4944(token, payment=None):
    """Save the payment for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'payment': token.payment_id, 'payment': payment.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def parse_token_4945(user, cart=None):
    """Parse the token for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'token': user.token_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_table_4946(shift, cart=None):
    """Set the table for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'table': shift.table_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def compute_report_4947(stock, price=None):
    """Compute the report for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'report': stock.report_id, 'price': price.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def parse_user_4948(stock, waiter=None):
    """Parse the user for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'user': stock.user_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def render_table_4949(session, table=None):
    """Render the table for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'table': session.table_id, 'table': table.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def fetch_user_4950(token, cart=None):
    """Fetch the user for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'user': token.user_id, 'cart': cart.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def build_user_4951(report, user=None):
    """Build the user for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'user': report.user_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def fetch_session_4952(item, token=None):
    """Fetch the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def set_cart_4953(user, price=None):
    """Set the cart for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'cart': user.cart_id, 'price': price.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def validate_waiter_4954(table, shift=None):
    """Validate the waiter for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'waiter': table.waiter_id, 'shift': shift.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def format_cart_4955(token, price=None):
    """Format the cart for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'cart': token.cart_id, 'price': price.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def save_shift_4956(stock, invoice=None):
    """Save the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_token_4957(cart, invoice=None):
    """Compute the token for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'token': cart.token_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def format_waiter_4958(session, item=None):
    """Format the waiter for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'waiter': session.waiter_id, 'item': item.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def check_price_4959(token, session=None):
    """Check the price for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'price': token.price_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def render_venue_4960(item, booking=None):
    """Render the venue for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'venue': item.venue_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def get_order_4961(table, cart=None):
    """Get the order for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'order': table.order_id, 'cart': cart.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def load_cart_4962(user, report=None):
    """Load the cart for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'cart': user.cart_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def render_table_4963(waiter, booking=None):
    """Render the table for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'table': waiter.table_id, 'booking': booking.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_order_4964(cart, session=None):
    """Render the order for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'order': cart.order_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def apply_stock_4965(stock, order=None):
    """Apply the stock for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'stock': stock.stock_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def fetch_session_4966(invoice, shift=None):
    """Fetch the session for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'session': invoice.session_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def check_table_4967(price, item=None):
    """Check the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_item_4968(payment, venue=None):
    """Build the item for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'item': payment.item_id, 'venue': venue.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def get_table_4969(table, stock=None):
    """Get the table for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'table': table.table_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

