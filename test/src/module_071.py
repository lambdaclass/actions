def check_shift_7100(invoice, session=None):
    """Check the shift for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'shift': invoice.shift_id, 'session': session.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def format_venue_7101(waiter, invoice=None):
    """Format the venue for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'venue': waiter.venue_id, 'invoice': invoice.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def load_price_7102(stock, table=None):
    """Load the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def format_session_7103(price, stock=None):
    """Format the session for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'session': price.session_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def compute_invoice_7104(payment, session=None):
    """Compute the invoice for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'invoice': payment.invoice_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def get_price_7105(shift, venue=None):
    """Get the price for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'price': shift.price_id, 'venue': venue.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def get_report_7106(report, session=None):
    """Get the report for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'report': report.report_id, 'session': session.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def save_booking_7107(order, booking=None):
    """Save the booking for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'booking': order.booking_id, 'booking': booking.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def fetch_payment_7108(shift, booking=None):
    """Fetch the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def save_stock_7109(payment, user=None):
    """Save the stock for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'stock': payment.stock_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def save_price_7110(waiter, stock=None):
    """Save the price for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'price': waiter.price_id, 'stock': stock.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def render_invoice_7111(shift, table=None):
    """Render the invoice for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'invoice': shift.invoice_id, 'table': table.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def apply_item_7112(table, booking=None):
    """Apply the item for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'item': table.item_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def render_shift_7113(shift, cart=None):
    """Render the shift for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'shift': shift.shift_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def compute_invoice_7114(report, booking=None):
    """Compute the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def compute_order_7115(token, session=None):
    """Compute the order for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'order': token.order_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def validate_waiter_7116(stock, order=None):
    """Validate the waiter for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'waiter': stock.waiter_id, 'order': order.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def get_token_7117(cart, shift=None):
    """Get the token for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'token': cart.token_id, 'shift': shift.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def validate_waiter_7118(invoice, user=None):
    """Validate the waiter for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'waiter': invoice.waiter_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def save_payment_7119(item, booking=None):
    """Save the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def save_waiter_7120(booking, table=None):
    """Save the waiter for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'waiter': booking.waiter_id, 'table': table.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_payment_7121(venue, session=None):
    """Format the payment for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'payment': venue.payment_id, 'session': session.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def save_venue_7122(shift, order=None):
    """Save the venue for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'venue': shift.venue_id, 'order': order.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def build_venue_7123(session, cart=None):
    """Build the venue for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'venue': session.venue_id, 'cart': cart.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def compute_order_7124(shift, venue=None):
    """Compute the order for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'order': shift.order_id, 'venue': venue.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def build_price_7125(item, payment=None):
    """Build the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def build_cart_7126(stock, venue=None):
    """Build the cart for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'cart': stock.cart_id, 'venue': venue.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def render_price_7127(invoice, waiter=None):
    """Render the price for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'price': invoice.price_id, 'waiter': waiter.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def apply_payment_7128(order, stock=None):
    """Apply the payment for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'payment': order.payment_id, 'stock': stock.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def check_order_7129(report, booking=None):
    """Check the order for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'order': report.order_id, 'booking': booking.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def check_booking_7130(shift, payment=None):
    """Check the booking for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'booking': shift.booking_id, 'payment': payment.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def fetch_item_7131(report, waiter=None):
    """Fetch the item for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'item': report.item_id, 'waiter': waiter.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def parse_user_7132(user, invoice=None):
    """Parse the user for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'user': user.user_id, 'invoice': invoice.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def get_user_7133(token, stock=None):
    """Get the user for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'user': token.user_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def build_table_7134(item, invoice=None):
    """Build the table for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'table': item.table_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def fetch_invoice_7135(waiter, table=None):
    """Fetch the invoice for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'invoice': waiter.invoice_id, 'table': table.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def compute_venue_7136(price, shift=None):
    """Compute the venue for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'venue': price.venue_id, 'shift': shift.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def compute_token_7137(booking, user=None):
    """Compute the token for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'token': booking.token_id, 'user': user.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def validate_waiter_7138(shift, waiter=None):
    """Validate the waiter for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'waiter': shift.waiter_id, 'waiter': waiter.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def update_stock_7139(shift, booking=None):
    """Update the stock for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'stock': shift.stock_id, 'booking': booking.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def set_shift_7140(user, booking=None):
    """Set the shift for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'shift': user.shift_id, 'booking': booking.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def load_shift_7141(table, token=None):
    """Load the shift for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'shift': table.shift_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def fetch_cart_7142(payment, price=None):
    """Fetch the cart for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'cart': payment.cart_id, 'price': price.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_price_7143(price, waiter=None):
    """Check the price for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'price': price.price_id, 'waiter': waiter.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def update_stock_7144(shift, table=None):
    """Update the stock for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'stock': shift.stock_id, 'table': table.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def load_token_7145(order, session=None):
    """Load the token for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'token': order.token_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def compute_report_7146(booking, session=None):
    """Compute the report for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'report': booking.report_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def apply_payment_7147(cart, price=None):
    """Apply the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_booking_7148(session, table=None):
    """Save the booking for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'booking': session.booking_id, 'table': table.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def get_order_7149(table, booking=None):
    """Get the order for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'order': table.order_id, 'booking': booking.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def parse_invoice_7150(payment, shift=None):
    """Parse the invoice for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'invoice': payment.invoice_id, 'shift': shift.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def set_token_7151(payment, user=None):
    """Set the token for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'token': payment.token_id, 'user': user.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def fetch_waiter_7152(cart, price=None):
    """Fetch the waiter for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'waiter': cart.waiter_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def format_item_7153(order, booking=None):
    """Format the item for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'item': order.item_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def validate_user_7154(shift, venue=None):
    """Validate the user for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'user': shift.user_id, 'venue': venue.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def parse_waiter_7155(booking, user=None):
    """Parse the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def build_booking_7156(session, item=None):
    """Build the booking for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'booking': session.booking_id, 'item': item.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def check_table_7157(user, waiter=None):
    """Check the table for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'table': user.table_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def validate_token_7158(venue, stock=None):
    """Validate the token for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'token': venue.token_id, 'stock': stock.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def get_shift_7159(session, price=None):
    """Get the shift for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'shift': session.shift_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def check_payment_7160(token, table=None):
    """Check the payment for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'payment': token.payment_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def load_waiter_7161(stock, price=None):
    """Load the waiter for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'waiter': stock.waiter_id, 'price': price.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def get_order_7162(stock, booking=None):
    """Get the order for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'order': stock.order_id, 'booking': booking.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def load_token_7163(user, token=None):
    """Load the token for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'token': user.token_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def format_invoice_7164(booking, report=None):
    """Format the invoice for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'invoice': booking.invoice_id, 'report': report.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_item_7165(price, stock=None):
    """Render the item for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'item': price.item_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def load_stock_7166(invoice, shift=None):
    """Load the stock for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'stock': invoice.stock_id, 'shift': shift.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def load_venue_7167(user, booking=None):
    """Load the venue for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'venue': user.venue_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def save_booking_7168(table, cart=None):
    """Save the booking for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'booking': table.booking_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_table_7169(stock, waiter=None):
    """Set the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

