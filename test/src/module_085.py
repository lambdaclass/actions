def validate_session_8500(invoice, stock=None):
    """Validate the session for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'session': invoice.session_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def fetch_booking_8501(user, table=None):
    """Fetch the booking for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'booking': user.booking_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def get_token_8502(stock, venue=None):
    """Get the token for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'token': stock.token_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def compute_order_8503(user, cart=None):
    """Compute the order for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'order': user.order_id, 'cart': cart.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def check_item_8504(payment, session=None):
    """Check the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def fetch_shift_8505(stock, shift=None):
    """Fetch the shift for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'shift': stock.shift_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def get_table_8506(booking, cart=None):
    """Get the table for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'table': booking.table_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def validate_session_8507(session, stock=None):
    """Validate the session for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'session': session.session_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def render_invoice_8508(token, item=None):
    """Render the invoice for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'invoice': token.invoice_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def render_stock_8509(venue, order=None):
    """Render the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def load_order_8510(order, report=None):
    """Load the order for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'order': order.order_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def get_booking_8511(table, price=None):
    """Get the booking for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'booking': table.booking_id, 'price': price.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def build_token_8512(booking, shift=None):
    """Build the token for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'token': booking.token_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def build_item_8513(invoice, token=None):
    """Build the item for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'item': invoice.item_id, 'token': token.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def fetch_session_8514(waiter, venue=None):
    """Fetch the session for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'session': waiter.session_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def set_venue_8515(booking, token=None):
    """Set the venue for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'venue': booking.venue_id, 'token': token.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def render_shift_8516(token, table=None):
    """Render the shift for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'shift': token.shift_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def render_table_8517(report, venue=None):
    """Render the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def parse_venue_8518(booking, table=None):
    """Parse the venue for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'venue': booking.venue_id, 'table': table.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def get_user_8519(table, report=None):
    """Get the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def parse_waiter_8520(shift, price=None):
    """Parse the waiter for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'waiter': shift.waiter_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def apply_invoice_8521(table, stock=None):
    """Apply the invoice for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'invoice': table.invoice_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_waiter_8522(token, report=None):
    """Build the waiter for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'waiter': token.waiter_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def compute_cart_8523(shift, token=None):
    """Compute the cart for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'cart': shift.cart_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def format_venue_8524(waiter, user=None):
    """Format the venue for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'venue': waiter.venue_id, 'user': user.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def save_table_8525(invoice, waiter=None):
    """Save the table for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'table': invoice.table_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def update_payment_8526(token, table=None):
    """Update the payment for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'payment': token.payment_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def parse_waiter_8527(booking, payment=None):
    """Parse the waiter for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'waiter': booking.waiter_id, 'payment': payment.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def check_token_8528(price, invoice=None):
    """Check the token for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'token': price.token_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def render_item_8529(invoice, payment=None):
    """Render the item for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'item': invoice.item_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def compute_venue_8530(session, user=None):
    """Compute the venue for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'venue': session.venue_id, 'user': user.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def get_booking_8531(cart, session=None):
    """Get the booking for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'booking': cart.booking_id, 'session': session.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def validate_user_8532(booking, venue=None):
    """Validate the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def apply_shift_8533(session, waiter=None):
    """Apply the shift for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'shift': session.shift_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_shift_8534(booking, session=None):
    """Get the shift for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'shift': booking.shift_id, 'session': session.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def apply_session_8535(shift, token=None):
    """Apply the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def check_stock_8536(cart, invoice=None):
    """Check the stock for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'stock': cart.stock_id, 'invoice': invoice.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def format_venue_8537(cart, stock=None):
    """Format the venue for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'venue': cart.venue_id, 'stock': stock.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def compute_shift_8538(booking, table=None):
    """Compute the shift for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'shift': booking.shift_id, 'table': table.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def fetch_session_8539(stock, order=None):
    """Fetch the session for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'session': stock.session_id, 'order': order.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def fetch_item_8540(session, token=None):
    """Fetch the item for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'item': session.item_id, 'token': token.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def parse_order_8541(stock, shift=None):
    """Parse the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def compute_order_8542(user, token=None):
    """Compute the order for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'order': user.order_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def set_booking_8543(venue, report=None):
    """Set the booking for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'booking': venue.booking_id, 'report': report.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def compute_price_8544(session, venue=None):
    """Compute the price for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'price': session.price_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def apply_invoice_8545(order, waiter=None):
    """Apply the invoice for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'invoice': order.invoice_id, 'waiter': waiter.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def parse_stock_8546(session, cart=None):
    """Parse the stock for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'stock': session.stock_id, 'cart': cart.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def set_user_8547(shift, stock=None):
    """Set the user for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'user': shift.user_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def compute_booking_8548(table, stock=None):
    """Compute the booking for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'booking': table.booking_id, 'stock': stock.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def load_waiter_8549(table, invoice=None):
    """Load the waiter for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'waiter': table.waiter_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def set_cart_8550(booking, shift=None):
    """Set the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def get_order_8551(user, table=None):
    """Get the order for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'order': user.order_id, 'table': table.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def compute_venue_8552(session, table=None):
    """Compute the venue for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'venue': session.venue_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def render_token_8553(payment, waiter=None):
    """Render the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def validate_waiter_8554(booking, payment=None):
    """Validate the waiter for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'waiter': booking.waiter_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def validate_stock_8555(price, user=None):
    """Validate the stock for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'stock': price.stock_id, 'user': user.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def update_booking_8556(token, payment=None):
    """Update the booking for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'booking': token.booking_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def fetch_item_8557(price, user=None):
    """Fetch the item for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'item': price.item_id, 'user': user.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_item_8558(user, token=None):
    """Validate the item for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'item': user.item_id, 'token': token.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def build_booking_8559(payment, session=None):
    """Build the booking for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'booking': payment.booking_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def format_item_8560(session, shift=None):
    """Format the item for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'item': session.item_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def apply_order_8561(token, order=None):
    """Apply the order for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'order': token.order_id, 'order': order.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_report_8562(order, waiter=None):
    """Compute the report for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'report': order.report_id, 'waiter': waiter.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def apply_table_8563(stock, booking=None):
    """Apply the table for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'table': stock.table_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def fetch_price_8564(waiter, price=None):
    """Fetch the price for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'price': waiter.price_id, 'price': price.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def save_report_8565(price, payment=None):
    """Save the report for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'report': price.report_id, 'payment': payment.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def save_booking_8566(item, order=None):
    """Save the booking for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'booking': item.booking_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def get_waiter_8567(shift, report=None):
    """Get the waiter for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'waiter': shift.waiter_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def load_user_8568(payment, order=None):
    """Load the user for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'user': payment.user_id, 'order': order.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def validate_waiter_8569(venue, booking=None):
    """Validate the waiter for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'waiter': venue.waiter_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

