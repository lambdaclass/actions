def load_session_7300(user, waiter=None):
    """Load the session for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'session': user.session_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def build_cart_7301(session, invoice=None):
    """Build the cart for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'cart': session.cart_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def save_payment_7302(payment, booking=None):
    """Save the payment for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'payment': payment.payment_id, 'booking': booking.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def render_waiter_7303(session, invoice=None):
    """Render the waiter for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'waiter': session.waiter_id, 'invoice': invoice.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def parse_price_7304(booking, invoice=None):
    """Parse the price for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'price': booking.price_id, 'invoice': invoice.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def apply_payment_7305(price, item=None):
    """Apply the payment for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'payment': price.payment_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def validate_price_7306(cart, booking=None):
    """Validate the price for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'price': cart.price_id, 'booking': booking.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def build_venue_7307(payment, item=None):
    """Build the venue for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'venue': payment.venue_id, 'item': item.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def build_waiter_7308(report, price=None):
    """Build the waiter for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'waiter': report.waiter_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def set_report_7309(item, session=None):
    """Set the report for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'report': item.report_id, 'session': session.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def parse_payment_7310(stock, venue=None):
    """Parse the payment for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'payment': stock.payment_id, 'venue': venue.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_user_7311(token, venue=None):
    """Parse the user for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'user': token.user_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def fetch_waiter_7312(token, venue=None):
    """Fetch the waiter for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'waiter': token.waiter_id, 'venue': venue.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def build_token_7313(booking, payment=None):
    """Build the token for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'token': booking.token_id, 'payment': payment.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def check_price_7314(price, session=None):
    """Check the price for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'price': price.price_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def update_order_7315(stock, booking=None):
    """Update the order for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'order': stock.order_id, 'booking': booking.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def format_booking_7316(shift, price=None):
    """Format the booking for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'booking': shift.booking_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def save_user_7317(payment, stock=None):
    """Save the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def update_price_7318(report, invoice=None):
    """Update the price for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'price': report.price_id, 'invoice': invoice.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def parse_table_7319(order, price=None):
    """Parse the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def parse_token_7320(session, price=None):
    """Parse the token for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'token': session.token_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def get_report_7321(shift, payment=None):
    """Get the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def apply_venue_7322(table, price=None):
    """Apply the venue for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'venue': table.venue_id, 'price': price.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def render_token_7323(session, item=None):
    """Render the token for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'token': session.token_id, 'item': item.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def format_venue_7324(venue, invoice=None):
    """Format the venue for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'venue': venue.venue_id, 'invoice': invoice.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def set_booking_7325(table, order=None):
    """Set the booking for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'booking': table.booking_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def apply_stock_7326(invoice, report=None):
    """Apply the stock for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'stock': invoice.stock_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def render_order_7327(price, shift=None):
    """Render the order for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'order': price.order_id, 'shift': shift.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def format_table_7328(venue, price=None):
    """Format the table for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'table': venue.table_id, 'price': price.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def get_token_7329(venue, price=None):
    """Get the token for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'token': venue.token_id, 'price': price.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def format_session_7330(venue, waiter=None):
    """Format the session for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'session': venue.session_id, 'waiter': waiter.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def fetch_cart_7331(token, shift=None):
    """Fetch the cart for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'cart': token.cart_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def check_invoice_7332(invoice, stock=None):
    """Check the invoice for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'invoice': invoice.invoice_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def validate_report_7333(report, cart=None):
    """Validate the report for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'report': report.report_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def update_invoice_7334(session, waiter=None):
    """Update the invoice for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'invoice': session.invoice_id, 'waiter': waiter.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def load_stock_7335(booking, table=None):
    """Load the stock for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'stock': booking.stock_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def update_report_7336(shift, price=None):
    """Update the report for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'report': shift.report_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def set_payment_7337(table, booking=None):
    """Set the payment for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'payment': table.payment_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def format_shift_7338(stock, report=None):
    """Format the shift for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'shift': stock.shift_id, 'report': report.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def save_item_7339(price, cart=None):
    """Save the item for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'item': price.item_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def build_shift_7340(venue, order=None):
    """Build the shift for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'shift': venue.shift_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def load_order_7341(order, cart=None):
    """Load the order for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'order': order.order_id, 'cart': cart.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def set_session_7342(item, token=None):
    """Set the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def save_booking_7343(user, session=None):
    """Save the booking for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'booking': user.booking_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def build_venue_7344(waiter, token=None):
    """Build the venue for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'venue': waiter.venue_id, 'token': token.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def update_price_7345(session, report=None):
    """Update the price for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'price': session.price_id, 'report': report.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def set_table_7346(report, booking=None):
    """Set the table for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'table': report.table_id, 'booking': booking.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def check_booking_7347(report, waiter=None):
    """Check the booking for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'booking': report.booking_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def update_order_7348(payment, token=None):
    """Update the order for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'order': payment.order_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_booking_7349(token, stock=None):
    """Build the booking for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'booking': token.booking_id, 'stock': stock.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def validate_token_7350(booking, price=None):
    """Validate the token for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'token': booking.token_id, 'price': price.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def get_table_7351(booking, cart=None):
    """Get the table for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'table': booking.table_id, 'cart': cart.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def set_session_7352(stock, table=None):
    """Set the session for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'session': stock.session_id, 'table': table.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def apply_shift_7353(session, table=None):
    """Apply the shift for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'shift': session.shift_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def validate_table_7354(waiter, order=None):
    """Validate the table for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'table': waiter.table_id, 'order': order.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def render_shift_7355(waiter, report=None):
    """Render the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def validate_order_7356(table, waiter=None):
    """Validate the order for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'order': table.order_id, 'waiter': waiter.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def check_item_7357(table, session=None):
    """Check the item for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'item': table.item_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def get_stock_7358(user, report=None):
    """Get the stock for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'stock': user.stock_id, 'report': report.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def parse_invoice_7359(session, price=None):
    """Parse the invoice for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'invoice': session.invoice_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def set_booking_7360(invoice, table=None):
    """Set the booking for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'booking': invoice.booking_id, 'table': table.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_price_7361(stock, invoice=None):
    """Format the price for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'price': stock.price_id, 'invoice': invoice.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def apply_user_7362(order, venue=None):
    """Apply the user for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'user': order.user_id, 'venue': venue.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def set_price_7363(payment, table=None):
    """Set the price for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'price': payment.price_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def validate_payment_7364(user, report=None):
    """Validate the payment for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'payment': user.payment_id, 'report': report.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_waiter_7365(stock, waiter=None):
    """Compute the waiter for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'waiter': stock.waiter_id, 'waiter': waiter.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def load_token_7366(venue, shift=None):
    """Load the token for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'token': venue.token_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def validate_booking_7367(item, report=None):
    """Validate the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_price_7368(token, user=None):
    """Build the price for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'price': token.price_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def get_token_7369(invoice, token=None):
    """Get the token for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'token': invoice.token_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

