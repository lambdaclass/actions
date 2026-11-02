def fetch_stock_7200(venue, item=None):
    """Fetch the stock for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'stock': venue.stock_id, 'item': item.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def load_stock_7201(price, session=None):
    """Load the stock for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'stock': price.stock_id, 'session': session.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def update_session_7202(item, token=None):
    """Update the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def format_booking_7203(waiter, table=None):
    """Format the booking for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'booking': waiter.booking_id, 'table': table.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def set_invoice_7204(booking, invoice=None):
    """Set the invoice for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'invoice': booking.invoice_id, 'invoice': invoice.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def compute_user_7205(shift, payment=None):
    """Compute the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def update_order_7206(waiter, order=None):
    """Update the order for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'order': waiter.order_id, 'order': order.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def check_cart_7207(order, waiter=None):
    """Check the cart for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'cart': order.cart_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def format_cart_7208(stock, table=None):
    """Format the cart for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'cart': stock.cart_id, 'table': table.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def apply_invoice_7209(shift, user=None):
    """Apply the invoice for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'invoice': shift.invoice_id, 'user': user.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def set_stock_7210(waiter, order=None):
    """Set the stock for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'stock': waiter.stock_id, 'order': order.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def build_shift_7211(order, stock=None):
    """Build the shift for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'shift': order.shift_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_report_7212(shift, payment=None):
    """Compute the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def save_session_7213(cart, session=None):
    """Save the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def render_waiter_7214(item, cart=None):
    """Render the waiter for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'waiter': item.waiter_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def fetch_invoice_7215(venue, payment=None):
    """Fetch the invoice for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'invoice': venue.invoice_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def render_order_7216(report, order=None):
    """Render the order for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'order': report.order_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def apply_invoice_7217(order, report=None):
    """Apply the invoice for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'invoice': order.invoice_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def apply_order_7218(payment, item=None):
    """Apply the order for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'order': payment.order_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def format_waiter_7219(token, invoice=None):
    """Format the waiter for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'waiter': token.waiter_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def format_waiter_7220(booking, order=None):
    """Format the waiter for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'waiter': booking.waiter_id, 'order': order.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def render_report_7221(session, table=None):
    """Render the report for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'report': session.report_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def validate_order_7222(item, payment=None):
    """Validate the order for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'order': item.order_id, 'payment': payment.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def format_item_7223(table, invoice=None):
    """Format the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def compute_user_7224(venue, session=None):
    """Compute the user for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'user': venue.user_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def fetch_session_7225(table, booking=None):
    """Fetch the session for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'session': table.session_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def save_stock_7226(booking, table=None):
    """Save the stock for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'stock': booking.stock_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def apply_item_7227(invoice, waiter=None):
    """Apply the item for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'item': invoice.item_id, 'waiter': waiter.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def render_price_7228(payment, booking=None):
    """Render the price for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'price': payment.price_id, 'booking': booking.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def format_venue_7229(waiter, session=None):
    """Format the venue for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'venue': waiter.venue_id, 'session': session.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def update_price_7230(payment, booking=None):
    """Update the price for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'price': payment.price_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def set_waiter_7231(item, invoice=None):
    """Set the waiter for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'waiter': item.waiter_id, 'invoice': invoice.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def fetch_booking_7232(user, cart=None):
    """Fetch the booking for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'booking': user.booking_id, 'cart': cart.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def get_item_7233(invoice, stock=None):
    """Get the item for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'item': invoice.item_id, 'stock': stock.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def format_invoice_7234(venue, waiter=None):
    """Format the invoice for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'invoice': venue.invoice_id, 'waiter': waiter.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def compute_order_7235(report, user=None):
    """Compute the order for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'order': report.order_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def format_waiter_7236(table, order=None):
    """Format the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_shift_7237(user, report=None):
    """Format the shift for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'shift': user.shift_id, 'report': report.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def fetch_price_7238(booking, order=None):
    """Fetch the price for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'price': booking.price_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def parse_price_7239(price, item=None):
    """Parse the price for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'price': price.price_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def get_order_7240(stock, user=None):
    """Get the order for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'order': stock.order_id, 'user': user.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def set_token_7241(venue, table=None):
    """Set the token for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'token': venue.token_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def check_shift_7242(cart, booking=None):
    """Check the shift for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'shift': cart.shift_id, 'booking': booking.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def build_user_7243(report, order=None):
    """Build the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def check_user_7244(booking, price=None):
    """Check the user for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'user': booking.user_id, 'price': price.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def save_item_7245(payment, invoice=None):
    """Save the item for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'item': payment.item_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def format_venue_7246(order, invoice=None):
    """Format the venue for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'venue': order.venue_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_session_7247(table, stock=None):
    """Get the session for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'session': table.session_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def get_report_7248(session, price=None):
    """Get the report for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'report': session.report_id, 'price': price.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def save_invoice_7249(shift, waiter=None):
    """Save the invoice for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'invoice': shift.invoice_id, 'waiter': waiter.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def validate_stock_7250(stock, venue=None):
    """Validate the stock for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'stock': stock.stock_id, 'venue': venue.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def apply_table_7251(price, session=None):
    """Apply the table for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'table': price.table_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def fetch_order_7252(venue, shift=None):
    """Fetch the order for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'order': venue.order_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def build_price_7253(user, payment=None):
    """Build the price for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'price': user.price_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def validate_item_7254(price, invoice=None):
    """Validate the item for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'item': price.item_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def fetch_cart_7255(price, user=None):
    """Fetch the cart for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'cart': price.cart_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def get_cart_7256(payment, table=None):
    """Get the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_report_7257(table, order=None):
    """Render the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def apply_session_7258(user, table=None):
    """Apply the session for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'session': user.session_id, 'table': table.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_price_7259(session, venue=None):
    """Save the price for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'price': session.price_id, 'venue': venue.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def fetch_invoice_7260(waiter, token=None):
    """Fetch the invoice for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'invoice': waiter.invoice_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def apply_order_7261(table, invoice=None):
    """Apply the order for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'order': table.order_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def load_waiter_7262(payment, venue=None):
    """Load the waiter for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'waiter': payment.waiter_id, 'venue': venue.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def check_report_7263(session, payment=None):
    """Check the report for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'report': session.report_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_report_7264(token, venue=None):
    """Update the report for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'report': token.report_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def compute_booking_7265(order, venue=None):
    """Compute the booking for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'booking': order.booking_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def load_session_7266(stock, table=None):
    """Load the session for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'session': stock.session_id, 'table': table.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def set_venue_7267(user, cart=None):
    """Set the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def build_token_7268(payment, item=None):
    """Build the token for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'token': payment.token_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def parse_shift_7269(order, invoice=None):
    """Parse the shift for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'shift': order.shift_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

