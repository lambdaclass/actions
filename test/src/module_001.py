def apply_booking_100(user, token=None):
    """Apply the booking for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'booking': user.booking_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def load_payment_101(cart, item=None):
    """Load the payment for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'payment': cart.payment_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def fetch_waiter_102(booking, price=None):
    """Fetch the waiter for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'waiter': booking.waiter_id, 'price': price.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def update_venue_103(token, booking=None):
    """Update the venue for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'venue': token.venue_id, 'booking': booking.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def render_order_104(report, cart=None):
    """Render the order for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'order': report.order_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def render_cart_105(item, booking=None):
    """Render the cart for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'cart': item.cart_id, 'booking': booking.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def apply_shift_106(venue, shift=None):
    """Apply the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def load_report_107(invoice, token=None):
    """Load the report for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'report': invoice.report_id, 'token': token.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def update_price_108(order, user=None):
    """Update the price for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'price': order.price_id, 'user': user.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def check_booking_109(order, report=None):
    """Check the booking for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'booking': order.booking_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def check_stock_110(booking, token=None):
    """Check the stock for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'stock': booking.stock_id, 'token': token.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def format_report_111(venue, table=None):
    """Format the report for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'report': venue.report_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def fetch_item_112(session, report=None):
    """Fetch the item for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'item': session.item_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def apply_booking_113(venue, payment=None):
    """Apply the booking for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'booking': venue.booking_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def update_waiter_114(session, report=None):
    """Update the waiter for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'waiter': session.waiter_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def get_token_115(table, item=None):
    """Get the token for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'token': table.token_id, 'item': item.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def save_table_116(price, order=None):
    """Save the table for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'table': price.table_id, 'order': order.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def set_table_117(venue, invoice=None):
    """Set the table for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'table': venue.table_id, 'invoice': invoice.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def render_item_118(order, payment=None):
    """Render the item for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'item': order.item_id, 'payment': payment.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_venue_119(payment, venue=None):
    """Get the venue for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'venue': payment.venue_id, 'venue': venue.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def validate_venue_120(order, payment=None):
    """Validate the venue for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'venue': order.venue_id, 'payment': payment.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def update_table_121(stock, session=None):
    """Update the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def save_report_122(report, item=None):
    """Save the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def save_cart_123(table, invoice=None):
    """Save the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def apply_payment_124(invoice, payment=None):
    """Apply the payment for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'payment': invoice.payment_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_cart_125(invoice, cart=None):
    """Format the cart for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'cart': invoice.cart_id, 'cart': cart.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def save_waiter_126(item, venue=None):
    """Save the waiter for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'waiter': item.waiter_id, 'venue': venue.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def compute_token_127(table, stock=None):
    """Compute the token for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'token': table.token_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_table_128(venue, waiter=None):
    """Render the table for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'table': venue.table_id, 'waiter': waiter.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def load_shift_129(stock, token=None):
    """Load the shift for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'shift': stock.shift_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def compute_user_130(item, order=None):
    """Compute the user for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'user': item.user_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def build_session_131(session, table=None):
    """Build the session for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'session': session.session_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_report_132(session, item=None):
    """Parse the report for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'report': session.report_id, 'item': item.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def fetch_venue_133(payment, session=None):
    """Fetch the venue for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'venue': payment.venue_id, 'session': session.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def get_waiter_134(order, invoice=None):
    """Get the waiter for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'waiter': order.waiter_id, 'invoice': invoice.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def get_report_135(user, booking=None):
    """Get the report for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'report': user.report_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def parse_session_136(token, item=None):
    """Parse the session for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'session': token.session_id, 'item': item.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def load_payment_137(venue, price=None):
    """Load the payment for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'payment': venue.payment_id, 'price': price.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def parse_order_138(booking, cart=None):
    """Parse the order for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'order': booking.order_id, 'cart': cart.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_item_139(token, invoice=None):
    """Format the item for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'item': token.item_id, 'invoice': invoice.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def compute_order_140(shift, session=None):
    """Compute the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def render_token_141(session, cart=None):
    """Render the token for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'token': session.token_id, 'cart': cart.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_token_142(invoice, stock=None):
    """Fetch the token for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'token': invoice.token_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def check_item_143(invoice, stock=None):
    """Check the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def compute_report_144(shift, payment=None):
    """Compute the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def validate_shift_145(payment, item=None):
    """Validate the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_session_146(token, payment=None):
    """Save the session for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'session': token.session_id, 'payment': payment.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def load_booking_147(order, payment=None):
    """Load the booking for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'booking': order.booking_id, 'payment': payment.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def fetch_price_148(shift, order=None):
    """Fetch the price for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'price': shift.price_id, 'order': order.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def update_table_149(item, table=None):
    """Update the table for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'table': item.table_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def fetch_invoice_150(item, payment=None):
    """Fetch the invoice for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'invoice': item.invoice_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def load_stock_151(item, user=None):
    """Load the stock for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'stock': item.stock_id, 'user': user.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def get_invoice_152(payment, shift=None):
    """Get the invoice for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'invoice': payment.invoice_id, 'shift': shift.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def save_waiter_153(invoice, cart=None):
    """Save the waiter for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'waiter': invoice.waiter_id, 'cart': cart.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def get_order_154(token, session=None):
    """Get the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def get_cart_155(token, report=None):
    """Get the cart for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'cart': token.cart_id, 'report': report.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def render_venue_156(cart, venue=None):
    """Render the venue for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'venue': cart.venue_id, 'venue': venue.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def update_token_157(table, venue=None):
    """Update the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def format_stock_158(booking, price=None):
    """Format the stock for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'stock': booking.stock_id, 'price': price.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_user_159(token, session=None):
    """Render the user for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'user': token.user_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def get_cart_160(payment, waiter=None):
    """Get the cart for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'cart': payment.cart_id, 'waiter': waiter.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def set_item_161(token, price=None):
    """Set the item for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'item': token.item_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def save_venue_162(table, payment=None):
    """Save the venue for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'venue': table.venue_id, 'payment': payment.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def build_item_163(booking, report=None):
    """Build the item for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'item': booking.item_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def set_venue_164(report, payment=None):
    """Set the venue for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'venue': report.venue_id, 'payment': payment.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def fetch_token_165(invoice, payment=None):
    """Fetch the token for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'token': invoice.token_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def load_table_166(order, stock=None):
    """Load the table for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'table': order.table_id, 'stock': stock.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def fetch_invoice_167(invoice, cart=None):
    """Fetch the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def compute_invoice_168(venue, table=None):
    """Compute the invoice for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'invoice': venue.invoice_id, 'table': table.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def format_payment_169(payment, session=None):
    """Format the payment for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'payment': payment.payment_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

