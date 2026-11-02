def parse_venue_12900(booking, price=None):
    """Parse the venue for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'venue': booking.venue_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def format_order_12901(price, session=None):
    """Format the order for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'order': price.order_id, 'session': session.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def update_stock_12902(price, item=None):
    """Update the stock for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'stock': price.stock_id, 'item': item.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def apply_user_12903(user, token=None):
    """Apply the user for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'user': user.user_id, 'token': token.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def fetch_waiter_12904(item, waiter=None):
    """Fetch the waiter for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'waiter': item.waiter_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def load_order_12905(report, shift=None):
    """Load the order for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'order': report.order_id, 'shift': shift.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def check_payment_12906(order, user=None):
    """Check the payment for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'payment': order.payment_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def save_price_12907(cart, item=None):
    """Save the price for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'price': cart.price_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def validate_token_12908(user, payment=None):
    """Validate the token for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'token': user.token_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def set_stock_12909(venue, payment=None):
    """Set the stock for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'stock': venue.stock_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def fetch_user_12910(report, booking=None):
    """Fetch the user for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'user': report.user_id, 'booking': booking.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def render_shift_12911(venue, cart=None):
    """Render the shift for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'shift': venue.shift_id, 'cart': cart.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_shift_12912(table, session=None):
    """Build the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def build_item_12913(session, invoice=None):
    """Build the item for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'item': session.item_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def update_table_12914(table, session=None):
    """Update the table for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'table': table.table_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def get_item_12915(table, invoice=None):
    """Get the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def fetch_payment_12916(report, item=None):
    """Fetch the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_invoice_12917(order, invoice=None):
    """Format the invoice for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'invoice': order.invoice_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def compute_price_12918(waiter, token=None):
    """Compute the price for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'price': waiter.price_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def get_invoice_12919(booking, shift=None):
    """Get the invoice for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'invoice': booking.invoice_id, 'shift': shift.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def load_report_12920(waiter, invoice=None):
    """Load the report for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'report': waiter.report_id, 'invoice': invoice.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def check_booking_12921(invoice, booking=None):
    """Check the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def set_session_12922(order, session=None):
    """Set the session for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'session': order.session_id, 'session': session.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def render_table_12923(user, order=None):
    """Render the table for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'table': user.table_id, 'order': order.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def compute_payment_12924(session, table=None):
    """Compute the payment for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'payment': session.payment_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def load_price_12925(report, token=None):
    """Load the price for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'price': report.price_id, 'token': token.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def build_item_12926(token, payment=None):
    """Build the item for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'item': token.item_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def render_cart_12927(price, session=None):
    """Render the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def compute_report_12928(waiter, table=None):
    """Compute the report for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'report': waiter.report_id, 'table': table.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def parse_token_12929(cart, report=None):
    """Parse the token for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'token': cart.token_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def build_report_12930(shift, report=None):
    """Build the report for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'report': shift.report_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def load_stock_12931(session, venue=None):
    """Load the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def apply_price_12932(user, session=None):
    """Apply the price for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'price': user.price_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def render_price_12933(venue, price=None):
    """Render the price for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'price': venue.price_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def build_order_12934(invoice, venue=None):
    """Build the order for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'order': invoice.order_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def set_booking_12935(invoice, table=None):
    """Set the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def compute_user_12936(order, user=None):
    """Compute the user for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'user': order.user_id, 'user': user.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def set_shift_12937(shift, stock=None):
    """Set the shift for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'shift': shift.shift_id, 'stock': stock.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_shift_12938(venue, shift=None):
    """Parse the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def parse_user_12939(user, item=None):
    """Parse the user for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'user': user.user_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def compute_item_12940(booking, invoice=None):
    """Compute the item for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'item': booking.item_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_token_12941(session, token=None):
    """Validate the token for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'token': session.token_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def validate_shift_12942(report, user=None):
    """Validate the shift for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'shift': report.shift_id, 'user': user.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def parse_table_12943(booking, token=None):
    """Parse the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def build_report_12944(report, item=None):
    """Build the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def save_table_12945(cart, payment=None):
    """Save the table for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'table': cart.table_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def save_invoice_12946(session, user=None):
    """Save the invoice for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'invoice': session.invoice_id, 'user': user.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def apply_token_12947(cart, payment=None):
    """Apply the token for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'token': cart.token_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def get_venue_12948(table, order=None):
    """Get the venue for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'venue': table.venue_id, 'order': order.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def build_cart_12949(invoice, table=None):
    """Build the cart for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'cart': invoice.cart_id, 'table': table.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def get_payment_12950(session, venue=None):
    """Get the payment for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'payment': session.payment_id, 'venue': venue.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def format_order_12951(booking, table=None):
    """Format the order for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'order': booking.order_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def check_cart_12952(payment, invoice=None):
    """Check the cart for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'cart': payment.cart_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def get_report_12953(waiter, shift=None):
    """Get the report for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'report': waiter.report_id, 'shift': shift.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def save_venue_12954(invoice, order=None):
    """Save the venue for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'venue': invoice.venue_id, 'order': order.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def load_session_12955(table, session=None):
    """Load the session for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'session': table.session_id, 'session': session.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_cart_12956(venue, session=None):
    """Build the cart for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'cart': venue.cart_id, 'session': session.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def set_token_12957(cart, price=None):
    """Set the token for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'token': cart.token_id, 'price': price.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def save_report_12958(shift, booking=None):
    """Save the report for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'report': shift.report_id, 'booking': booking.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def compute_waiter_12959(session, venue=None):
    """Compute the waiter for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'waiter': session.waiter_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def load_booking_12960(price, session=None):
    """Load the booking for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'booking': price.booking_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def parse_order_12961(invoice, user=None):
    """Parse the order for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'order': invoice.order_id, 'user': user.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def render_stock_12962(cart, shift=None):
    """Render the stock for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'stock': cart.stock_id, 'shift': shift.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def validate_order_12963(booking, token=None):
    """Validate the order for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'order': booking.order_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def fetch_order_12964(token, shift=None):
    """Fetch the order for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'order': token.order_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def save_invoice_12965(cart, user=None):
    """Save the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def build_cart_12966(session, stock=None):
    """Build the cart for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'cart': session.cart_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def apply_booking_12967(price, item=None):
    """Apply the booking for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'booking': price.booking_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def save_item_12968(waiter, report=None):
    """Save the item for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'item': waiter.item_id, 'report': report.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_token_12969(user, booking=None):
    """Update the token for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'token': user.token_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

