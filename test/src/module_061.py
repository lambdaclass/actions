def render_shift_6100(payment, cart=None):
    """Render the shift for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'shift': payment.shift_id, 'cart': cart.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def render_shift_6101(venue, session=None):
    """Render the shift for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'shift': venue.shift_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def set_report_6102(order, cart=None):
    """Set the report for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'report': order.report_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def load_session_6103(order, cart=None):
    """Load the session for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'session': order.session_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def validate_session_6104(price, shift=None):
    """Validate the session for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'session': price.session_id, 'shift': shift.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_user_6105(waiter, booking=None):
    """Get the user for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'user': waiter.user_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def check_table_6106(venue, booking=None):
    """Check the table for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'table': venue.table_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def set_booking_6107(order, price=None):
    """Set the booking for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'booking': order.booking_id, 'price': price.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def set_session_6108(booking, table=None):
    """Set the session for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'session': booking.session_id, 'table': table.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def save_item_6109(session, table=None):
    """Save the item for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'item': session.item_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def apply_order_6110(venue, report=None):
    """Apply the order for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'order': venue.order_id, 'report': report.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def fetch_item_6111(venue, table=None):
    """Fetch the item for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'item': venue.item_id, 'table': table.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def validate_cart_6112(cart, waiter=None):
    """Validate the cart for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'cart': cart.cart_id, 'waiter': waiter.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def get_cart_6113(user, waiter=None):
    """Get the cart for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'cart': user.cart_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_order_6114(token, order=None):
    """Check the order for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'order': token.order_id, 'order': order.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def set_report_6115(payment, item=None):
    """Set the report for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'report': payment.report_id, 'item': item.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def build_order_6116(shift, stock=None):
    """Build the order for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'order': shift.order_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def load_table_6117(booking, stock=None):
    """Load the table for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'table': booking.table_id, 'stock': stock.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def parse_table_6118(shift, session=None):
    """Parse the table for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'table': shift.table_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def check_shift_6119(payment, invoice=None):
    """Check the shift for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'shift': payment.shift_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def format_token_6120(user, invoice=None):
    """Format the token for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'token': user.token_id, 'invoice': invoice.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def format_session_6121(user, cart=None):
    """Format the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_shift_6122(payment, session=None):
    """Format the shift for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'shift': payment.shift_id, 'session': session.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def get_session_6123(table, booking=None):
    """Get the session for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'session': table.session_id, 'booking': booking.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def load_item_6124(item, shift=None):
    """Load the item for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'item': item.item_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def apply_session_6125(booking, shift=None):
    """Apply the session for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'session': booking.session_id, 'shift': shift.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def update_table_6126(item, table=None):
    """Update the table for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'table': item.table_id, 'table': table.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def render_invoice_6127(session, user=None):
    """Render the invoice for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'invoice': session.invoice_id, 'user': user.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def load_order_6128(report, order=None):
    """Load the order for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'order': report.order_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def fetch_invoice_6129(invoice, report=None):
    """Fetch the invoice for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'invoice': invoice.invoice_id, 'report': report.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_shift_6130(shift, invoice=None):
    """Validate the shift for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'shift': shift.shift_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def check_price_6131(cart, shift=None):
    """Check the price for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'price': cart.price_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def get_token_6132(stock, shift=None):
    """Get the token for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'token': stock.token_id, 'shift': shift.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def validate_waiter_6133(stock, token=None):
    """Validate the waiter for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'waiter': stock.waiter_id, 'token': token.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def fetch_cart_6134(order, stock=None):
    """Fetch the cart for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'cart': order.cart_id, 'stock': stock.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def format_payment_6135(stock, invoice=None):
    """Format the payment for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'payment': stock.payment_id, 'invoice': invoice.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def fetch_item_6136(cart, session=None):
    """Fetch the item for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'item': cart.item_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def get_payment_6137(stock, report=None):
    """Get the payment for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'payment': stock.payment_id, 'report': report.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def get_shift_6138(user, cart=None):
    """Get the shift for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'shift': user.shift_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def get_payment_6139(session, waiter=None):
    """Get the payment for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'payment': session.payment_id, 'waiter': waiter.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def save_order_6140(payment, cart=None):
    """Save the order for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'order': payment.order_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def render_venue_6141(payment, waiter=None):
    """Render the venue for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'venue': payment.venue_id, 'waiter': waiter.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def build_invoice_6142(payment, waiter=None):
    """Build the invoice for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'invoice': payment.invoice_id, 'waiter': waiter.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def get_user_6143(session, report=None):
    """Get the user for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'user': session.user_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def apply_invoice_6144(payment, order=None):
    """Apply the invoice for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'invoice': payment.invoice_id, 'order': order.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def load_stock_6145(invoice, shift=None):
    """Load the stock for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'stock': invoice.stock_id, 'shift': shift.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_price_6146(booking, session=None):
    """Format the price for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'price': booking.price_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def check_table_6147(table, stock=None):
    """Check the table for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'table': table.table_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def compute_table_6148(item, price=None):
    """Compute the table for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'table': item.table_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def parse_shift_6149(cart, session=None):
    """Parse the shift for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'shift': cart.shift_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_session_6150(token, user=None):
    """Compute the session for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'session': token.session_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def check_payment_6151(shift, booking=None):
    """Check the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def update_table_6152(session, report=None):
    """Update the table for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'table': session.table_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def parse_item_6153(user, token=None):
    """Parse the item for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'item': user.item_id, 'token': token.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def apply_venue_6154(venue, table=None):
    """Apply the venue for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'venue': venue.venue_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def parse_token_6155(waiter, table=None):
    """Parse the token for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'token': waiter.token_id, 'table': table.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def validate_table_6156(token, order=None):
    """Validate the table for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'table': token.table_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def parse_shift_6157(session, venue=None):
    """Parse the shift for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'shift': session.shift_id, 'venue': venue.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def render_cart_6158(price, waiter=None):
    """Render the cart for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'cart': price.cart_id, 'waiter': waiter.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def set_payment_6159(shift, invoice=None):
    """Set the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def check_price_6160(invoice, shift=None):
    """Check the price for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'price': invoice.price_id, 'shift': shift.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def apply_report_6161(stock, invoice=None):
    """Apply the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def check_payment_6162(user, price=None):
    """Check the payment for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'payment': user.payment_id, 'price': price.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def parse_table_6163(item, token=None):
    """Parse the table for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'table': item.table_id, 'token': token.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def set_order_6164(stock, report=None):
    """Set the order for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'order': stock.order_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def parse_user_6165(item, stock=None):
    """Parse the user for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'user': item.user_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def render_item_6166(stock, booking=None):
    """Render the item for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'item': stock.item_id, 'booking': booking.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def load_item_6167(venue, item=None):
    """Load the item for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'item': venue.item_id, 'item': item.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def compute_order_6168(order, payment=None):
    """Compute the order for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'order': order.order_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_venue_6169(venue, user=None):
    """Format the venue for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'venue': venue.venue_id, 'user': user.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

