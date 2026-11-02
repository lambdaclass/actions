def fetch_table_7600(venue, invoice=None):
    """Fetch the table for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'table': venue.table_id, 'invoice': invoice.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def validate_booking_7601(order, waiter=None):
    """Validate the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_stock_7602(cart, session=None):
    """Format the stock for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'stock': cart.stock_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def compute_payment_7603(payment, stock=None):
    """Compute the payment for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'payment': payment.payment_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def build_venue_7604(price, cart=None):
    """Build the venue for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'venue': price.venue_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def render_table_7605(waiter, venue=None):
    """Render the table for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'table': waiter.table_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def set_user_7606(token, report=None):
    """Set the user for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'user': token.user_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def fetch_item_7607(report, token=None):
    """Fetch the item for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'item': report.item_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def render_cart_7608(order, report=None):
    """Render the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def format_booking_7609(venue, booking=None):
    """Format the booking for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'booking': venue.booking_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def set_shift_7610(booking, cart=None):
    """Set the shift for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'shift': booking.shift_id, 'cart': cart.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def apply_waiter_7611(price, invoice=None):
    """Apply the waiter for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'waiter': price.waiter_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def check_payment_7612(stock, booking=None):
    """Check the payment for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'payment': stock.payment_id, 'booking': booking.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def load_table_7613(invoice, payment=None):
    """Load the table for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'table': invoice.table_id, 'payment': payment.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def apply_venue_7614(user, cart=None):
    """Apply the venue for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'venue': user.venue_id, 'cart': cart.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def save_price_7615(venue, table=None):
    """Save the price for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'price': venue.price_id, 'table': table.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def parse_order_7616(shift, user=None):
    """Parse the order for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'order': shift.order_id, 'user': user.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def apply_report_7617(shift, table=None):
    """Apply the report for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'report': shift.report_id, 'table': table.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def get_session_7618(user, cart=None):
    """Get the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def format_waiter_7619(venue, report=None):
    """Format the waiter for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'waiter': venue.waiter_id, 'report': report.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def load_booking_7620(waiter, shift=None):
    """Load the booking for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'booking': waiter.booking_id, 'shift': shift.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def parse_order_7621(shift, session=None):
    """Parse the order for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'order': shift.order_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def parse_shift_7622(invoice, venue=None):
    """Parse the shift for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'shift': invoice.shift_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def save_waiter_7623(shift, invoice=None):
    """Save the waiter for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'waiter': shift.waiter_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def check_order_7624(report, order=None):
    """Check the order for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'order': report.order_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def build_token_7625(shift, stock=None):
    """Build the token for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'token': shift.token_id, 'stock': stock.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def validate_payment_7626(cart, table=None):
    """Validate the payment for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'payment': cart.payment_id, 'table': table.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def format_invoice_7627(report, invoice=None):
    """Format the invoice for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'invoice': report.invoice_id, 'invoice': invoice.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_invoice_7628(booking, order=None):
    """Parse the invoice for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'invoice': booking.invoice_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def set_report_7629(booking, session=None):
    """Set the report for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'report': booking.report_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def save_waiter_7630(payment, item=None):
    """Save the waiter for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'waiter': payment.waiter_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def save_table_7631(order, shift=None):
    """Save the table for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'table': order.table_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def format_booking_7632(invoice, booking=None):
    """Format the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_shift_7633(session, invoice=None):
    """Format the shift for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'shift': session.shift_id, 'invoice': invoice.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def check_shift_7634(waiter, report=None):
    """Check the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def build_user_7635(session, user=None):
    """Build the user for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'user': session.user_id, 'user': user.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def format_cart_7636(venue, token=None):
    """Format the cart for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'cart': venue.cart_id, 'token': token.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def fetch_table_7637(item, stock=None):
    """Fetch the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def build_report_7638(invoice, order=None):
    """Build the report for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'report': invoice.report_id, 'order': order.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def get_stock_7639(invoice, cart=None):
    """Get the stock for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'stock': invoice.stock_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def apply_table_7640(shift, stock=None):
    """Apply the table for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'table': shift.table_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def set_cart_7641(stock, item=None):
    """Set the cart for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'cart': stock.cart_id, 'item': item.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def save_session_7642(invoice, item=None):
    """Save the session for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'session': invoice.session_id, 'item': item.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def compute_waiter_7643(user, shift=None):
    """Compute the waiter for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'waiter': user.waiter_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def render_cart_7644(price, token=None):
    """Render the cart for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'cart': price.cart_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def parse_table_7645(user, token=None):
    """Parse the table for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'table': user.table_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def get_table_7646(stock, shift=None):
    """Get the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def check_booking_7647(report, token=None):
    """Check the booking for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'booking': report.booking_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def set_booking_7648(waiter, session=None):
    """Set the booking for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'booking': waiter.booking_id, 'session': session.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def fetch_waiter_7649(user, token=None):
    """Fetch the waiter for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'waiter': user.waiter_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def set_invoice_7650(shift, token=None):
    """Set the invoice for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'invoice': shift.invoice_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def parse_token_7651(shift, invoice=None):
    """Parse the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def apply_price_7652(order, table=None):
    """Apply the price for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'price': order.price_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def compute_user_7653(shift, price=None):
    """Compute the user for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'user': shift.user_id, 'price': price.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def parse_item_7654(payment, token=None):
    """Parse the item for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'item': payment.item_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def compute_table_7655(session, venue=None):
    """Compute the table for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'table': session.table_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def fetch_shift_7656(venue, table=None):
    """Fetch the shift for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'shift': venue.shift_id, 'table': table.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def render_venue_7657(token, shift=None):
    """Render the venue for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'venue': token.venue_id, 'shift': shift.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def validate_token_7658(stock, table=None):
    """Validate the token for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'token': stock.token_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def render_booking_7659(booking, report=None):
    """Render the booking for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'booking': booking.booking_id, 'report': report.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def render_order_7660(item, stock=None):
    """Render the order for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'order': item.order_id, 'stock': stock.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def format_payment_7661(invoice, booking=None):
    """Format the payment for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'payment': invoice.payment_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def format_token_7662(token, waiter=None):
    """Format the token for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'token': token.token_id, 'waiter': waiter.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def update_shift_7663(token, table=None):
    """Update the shift for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'shift': token.shift_id, 'table': table.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def render_shift_7664(invoice, session=None):
    """Render the shift for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'shift': invoice.shift_id, 'session': session.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def set_item_7665(cart, price=None):
    """Set the item for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'item': cart.item_id, 'price': price.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def set_venue_7666(invoice, report=None):
    """Set the venue for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'venue': invoice.venue_id, 'report': report.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def apply_token_7667(invoice, token=None):
    """Apply the token for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'token': invoice.token_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def validate_venue_7668(item, shift=None):
    """Validate the venue for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'venue': item.venue_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_invoice_7669(item, invoice=None):
    """Validate the invoice for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'invoice': item.invoice_id, 'invoice': invoice.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

