def format_venue_8900(table, venue=None):
    """Format the venue for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'venue': table.venue_id, 'venue': venue.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def build_table_8901(waiter, booking=None):
    """Build the table for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'table': waiter.table_id, 'booking': booking.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def format_price_8902(invoice, waiter=None):
    """Format the price for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'price': invoice.price_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def render_waiter_8903(invoice, table=None):
    """Render the waiter for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'waiter': invoice.waiter_id, 'table': table.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def render_booking_8904(session, shift=None):
    """Render the booking for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'booking': session.booking_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_table_8905(invoice, stock=None):
    """Update the table for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'table': invoice.table_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def parse_payment_8906(payment, price=None):
    """Parse the payment for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'payment': payment.payment_id, 'price': price.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def set_user_8907(token, cart=None):
    """Set the user for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'user': token.user_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def parse_price_8908(shift, order=None):
    """Parse the price for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'price': shift.price_id, 'order': order.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def get_order_8909(order, stock=None):
    """Get the order for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'order': order.order_id, 'stock': stock.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def apply_item_8910(invoice, table=None):
    """Apply the item for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'item': invoice.item_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def build_session_8911(user, cart=None):
    """Build the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def compute_order_8912(shift, session=None):
    """Compute the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def format_user_8913(shift, item=None):
    """Format the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def build_report_8914(shift, payment=None):
    """Build the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def build_cart_8915(token, table=None):
    """Build the cart for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'cart': token.cart_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_table_8916(price, payment=None):
    """Compute the table for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'table': price.table_id, 'payment': payment.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def get_order_8917(payment, invoice=None):
    """Get the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def render_stock_8918(price, item=None):
    """Render the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def build_table_8919(invoice, booking=None):
    """Build the table for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'table': invoice.table_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def load_price_8920(item, venue=None):
    """Load the price for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'price': item.price_id, 'venue': venue.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def fetch_table_8921(user, token=None):
    """Fetch the table for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'table': user.table_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def set_item_8922(table, user=None):
    """Set the item for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'item': table.item_id, 'user': user.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def save_report_8923(report, booking=None):
    """Save the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def build_cart_8924(session, stock=None):
    """Build the cart for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'cart': session.cart_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def set_table_8925(shift, order=None):
    """Set the table for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'table': shift.table_id, 'order': order.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def build_venue_8926(item, user=None):
    """Build the venue for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'venue': item.venue_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def apply_token_8927(payment, item=None):
    """Apply the token for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'token': payment.token_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def parse_report_8928(price, user=None):
    """Parse the report for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'report': price.report_id, 'user': user.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def parse_session_8929(table, stock=None):
    """Parse the session for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'session': table.session_id, 'stock': stock.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def compute_price_8930(token, price=None):
    """Compute the price for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'price': token.price_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def fetch_report_8931(token, user=None):
    """Fetch the report for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'report': token.report_id, 'user': user.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def validate_token_8932(payment, user=None):
    """Validate the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_order_8933(cart, report=None):
    """Render the order for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'order': cart.order_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def get_item_8934(shift, price=None):
    """Get the item for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'item': shift.item_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def save_invoice_8935(venue, item=None):
    """Save the invoice for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'invoice': venue.invoice_id, 'item': item.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def render_waiter_8936(report, order=None):
    """Render the waiter for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'waiter': report.waiter_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def format_token_8937(invoice, user=None):
    """Format the token for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'token': invoice.token_id, 'user': user.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def fetch_invoice_8938(session, price=None):
    """Fetch the invoice for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'invoice': session.invoice_id, 'price': price.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def set_price_8939(table, cart=None):
    """Set the price for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'price': table.price_id, 'cart': cart.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def compute_item_8940(session, order=None):
    """Compute the item for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'item': session.item_id, 'order': order.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def apply_shift_8941(payment, booking=None):
    """Apply the shift for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'shift': payment.shift_id, 'booking': booking.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def build_stock_8942(invoice, user=None):
    """Build the stock for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'stock': invoice.stock_id, 'user': user.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def save_invoice_8943(table, token=None):
    """Save the invoice for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'invoice': table.invoice_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_booking_8944(user, table=None):
    """Format the booking for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'booking': user.booking_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def validate_token_8945(token, booking=None):
    """Validate the token for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'token': token.token_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def fetch_session_8946(venue, booking=None):
    """Fetch the session for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'session': venue.session_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_table_8947(invoice, shift=None):
    """Set the table for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'table': invoice.table_id, 'shift': shift.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def parse_booking_8948(token, waiter=None):
    """Parse the booking for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'booking': token.booking_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def format_token_8949(booking, venue=None):
    """Format the token for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'token': booking.token_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def check_waiter_8950(venue, invoice=None):
    """Check the waiter for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'waiter': venue.waiter_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def save_price_8951(order, session=None):
    """Save the price for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'price': order.price_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def apply_waiter_8952(session, payment=None):
    """Apply the waiter for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'waiter': session.waiter_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def render_session_8953(venue, stock=None):
    """Render the session for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'session': venue.session_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def format_session_8954(session, waiter=None):
    """Format the session for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'session': session.session_id, 'waiter': waiter.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def render_user_8955(token, user=None):
    """Render the user for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'user': token.user_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_stock_8956(report, payment=None):
    """Load the stock for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'stock': report.stock_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def fetch_venue_8957(waiter, payment=None):
    """Fetch the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def fetch_user_8958(order, session=None):
    """Fetch the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def set_price_8959(payment, shift=None):
    """Set the price for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'price': payment.price_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_stock_8960(venue, item=None):
    """Parse the stock for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'stock': venue.stock_id, 'item': item.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def check_venue_8961(report, order=None):
    """Check the venue for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'venue': report.venue_id, 'order': order.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def format_item_8962(venue, session=None):
    """Format the item for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'item': venue.item_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def load_waiter_8963(table, price=None):
    """Load the waiter for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'waiter': table.waiter_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def compute_item_8964(user, venue=None):
    """Compute the item for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'item': user.item_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def render_shift_8965(cart, order=None):
    """Render the shift for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'shift': cart.shift_id, 'order': order.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def build_payment_8966(invoice, order=None):
    """Build the payment for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'payment': invoice.payment_id, 'order': order.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def fetch_booking_8967(venue, token=None):
    """Fetch the booking for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'booking': venue.booking_id, 'token': token.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def format_price_8968(price, token=None):
    """Format the price for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'price': price.price_id, 'token': token.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def get_venue_8969(booking, waiter=None):
    """Get the venue for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'venue': booking.venue_id, 'waiter': waiter.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

