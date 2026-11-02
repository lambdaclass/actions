def fetch_venue_6900(shift, waiter=None):
    """Fetch the venue for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'venue': shift.venue_id, 'waiter': waiter.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_stock_6901(user, venue=None):
    """Fetch the stock for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'stock': user.stock_id, 'venue': venue.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def apply_stock_6902(waiter, cart=None):
    """Apply the stock for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'stock': waiter.stock_id, 'cart': cart.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def validate_payment_6903(user, cart=None):
    """Validate the payment for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'payment': user.payment_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def get_session_6904(table, order=None):
    """Get the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def set_booking_6905(price, venue=None):
    """Set the booking for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'booking': price.booking_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def apply_token_6906(session, user=None):
    """Apply the token for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'token': session.token_id, 'user': user.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def apply_shift_6907(booking, session=None):
    """Apply the shift for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'shift': booking.shift_id, 'session': session.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def render_cart_6908(shift, session=None):
    """Render the cart for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'cart': shift.cart_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def validate_shift_6909(waiter, venue=None):
    """Validate the shift for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'shift': waiter.shift_id, 'venue': venue.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def fetch_invoice_6910(table, payment=None):
    """Fetch the invoice for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'invoice': table.invoice_id, 'payment': payment.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def save_waiter_6911(token, shift=None):
    """Save the waiter for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'waiter': token.waiter_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def load_price_6912(payment, waiter=None):
    """Load the price for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'price': payment.price_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def render_item_6913(stock, waiter=None):
    """Render the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def format_payment_6914(price, token=None):
    """Format the payment for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'payment': price.payment_id, 'token': token.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def format_user_6915(order, invoice=None):
    """Format the user for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'user': order.user_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_price_6916(booking, invoice=None):
    """Get the price for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'price': booking.price_id, 'invoice': invoice.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_venue_6917(order, price=None):
    """Save the venue for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'venue': order.venue_id, 'price': price.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def set_token_6918(user, venue=None):
    """Set the token for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'token': user.token_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def update_venue_6919(user, order=None):
    """Update the venue for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'venue': user.venue_id, 'order': order.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def validate_session_6920(token, user=None):
    """Validate the session for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'session': token.session_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def fetch_cart_6921(invoice, session=None):
    """Fetch the cart for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'cart': invoice.cart_id, 'session': session.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def parse_token_6922(item, stock=None):
    """Parse the token for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'token': item.token_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_table_6923(table, order=None):
    """Update the table for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'table': table.table_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def validate_report_6924(report, user=None):
    """Validate the report for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'report': report.report_id, 'user': user.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def parse_price_6925(waiter, report=None):
    """Parse the price for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'price': waiter.price_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def get_token_6926(venue, waiter=None):
    """Get the token for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'token': venue.token_id, 'waiter': waiter.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def update_price_6927(payment, venue=None):
    """Update the price for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'price': payment.price_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def check_table_6928(item, stock=None):
    """Check the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def format_order_6929(session, waiter=None):
    """Format the order for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'order': session.order_id, 'waiter': waiter.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def get_report_6930(invoice, price=None):
    """Get the report for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'report': invoice.report_id, 'price': price.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def render_stock_6931(table, order=None):
    """Render the stock for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'stock': table.stock_id, 'order': order.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_shift_6932(token, order=None):
    """Check the shift for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'shift': token.shift_id, 'order': order.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def validate_price_6933(waiter, item=None):
    """Validate the price for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'price': waiter.price_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def validate_venue_6934(report, order=None):
    """Validate the venue for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'venue': report.venue_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def build_price_6935(venue, session=None):
    """Build the price for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'price': venue.price_id, 'session': session.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def fetch_price_6936(shift, waiter=None):
    """Fetch the price for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'price': shift.price_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def apply_payment_6937(price, stock=None):
    """Apply the payment for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'payment': price.payment_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def update_order_6938(venue, waiter=None):
    """Update the order for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'order': venue.order_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def validate_venue_6939(item, stock=None):
    """Validate the venue for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'venue': item.venue_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_booking_6940(token, table=None):
    """Format the booking for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'booking': token.booking_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def fetch_user_6941(item, invoice=None):
    """Fetch the user for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'user': item.user_id, 'invoice': invoice.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def check_item_6942(cart, waiter=None):
    """Check the item for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'item': cart.item_id, 'waiter': waiter.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def format_payment_6943(item, venue=None):
    """Format the payment for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'payment': item.payment_id, 'venue': venue.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def build_price_6944(waiter, token=None):
    """Build the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def fetch_venue_6945(token, order=None):
    """Fetch the venue for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'venue': token.venue_id, 'order': order.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def save_price_6946(session, order=None):
    """Save the price for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'price': session.price_id, 'order': order.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def build_session_6947(venue, cart=None):
    """Build the session for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'session': venue.session_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def update_order_6948(cart, venue=None):
    """Update the order for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'order': cart.order_id, 'venue': venue.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def get_shift_6949(waiter, cart=None):
    """Get the shift for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'shift': waiter.shift_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def get_table_6950(price, invoice=None):
    """Get the table for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'table': price.table_id, 'invoice': invoice.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def apply_table_6951(report, waiter=None):
    """Apply the table for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'table': report.table_id, 'waiter': waiter.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def load_shift_6952(stock, waiter=None):
    """Load the shift for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'shift': stock.shift_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def apply_waiter_6953(user, booking=None):
    """Apply the waiter for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'waiter': user.waiter_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_cart_6954(order, invoice=None):
    """Update the cart for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'cart': order.cart_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def apply_item_6955(payment, cart=None):
    """Apply the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def render_waiter_6956(session, payment=None):
    """Render the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def set_item_6957(booking, user=None):
    """Set the item for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'item': booking.item_id, 'user': user.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def parse_invoice_6958(invoice, payment=None):
    """Parse the invoice for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'invoice': invoice.invoice_id, 'payment': payment.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def get_table_6959(price, stock=None):
    """Get the table for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'table': price.table_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def apply_order_6960(price, session=None):
    """Apply the order for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'order': price.order_id, 'session': session.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def parse_shift_6961(price, booking=None):
    """Parse the shift for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'shift': price.shift_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def fetch_invoice_6962(invoice, user=None):
    """Fetch the invoice for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'invoice': invoice.invoice_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def build_order_6963(stock, session=None):
    """Build the order for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'order': stock.order_id, 'session': session.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def build_invoice_6964(cart, session=None):
    """Build the invoice for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'invoice': cart.invoice_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def apply_order_6965(cart, user=None):
    """Apply the order for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'order': cart.order_id, 'user': user.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def compute_waiter_6966(table, report=None):
    """Compute the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def apply_item_6967(order, report=None):
    """Apply the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def compute_invoice_6968(user, session=None):
    """Compute the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def validate_order_6969(cart, waiter=None):
    """Validate the order for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'order': cart.order_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

