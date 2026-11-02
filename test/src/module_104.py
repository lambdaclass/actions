def get_item_10400(stock, report=None):
    """Get the item for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'item': stock.item_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def render_cart_10401(order, shift=None):
    """Render the cart for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'cart': order.cart_id, 'shift': shift.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def fetch_token_10402(invoice, table=None):
    """Fetch the token for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'token': invoice.token_id, 'table': table.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def load_booking_10403(cart, shift=None):
    """Load the booking for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'booking': cart.booking_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def validate_order_10404(waiter, report=None):
    """Validate the order for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'order': waiter.order_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def format_cart_10405(booking, order=None):
    """Format the cart for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'cart': booking.cart_id, 'order': order.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def load_token_10406(item, cart=None):
    """Load the token for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'token': item.token_id, 'cart': cart.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def load_order_10407(invoice, venue=None):
    """Load the order for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'order': invoice.order_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def parse_stock_10408(token, payment=None):
    """Parse the stock for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'stock': token.stock_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def build_stock_10409(shift, payment=None):
    """Build the stock for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'stock': shift.stock_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def validate_session_10410(session, item=None):
    """Validate the session for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'session': session.session_id, 'item': item.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def compute_payment_10411(table, invoice=None):
    """Compute the payment for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'payment': table.payment_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def format_session_10412(item, booking=None):
    """Format the session for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'session': item.session_id, 'booking': booking.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def format_table_10413(order, table=None):
    """Format the table for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'table': order.table_id, 'table': table.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def format_session_10414(price, booking=None):
    """Format the session for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'session': price.session_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def parse_report_10415(stock, invoice=None):
    """Parse the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def check_booking_10416(venue, order=None):
    """Check the booking for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'booking': venue.booking_id, 'order': order.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def apply_order_10417(payment, booking=None):
    """Apply the order for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'order': payment.order_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def load_token_10418(shift, table=None):
    """Load the token for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'token': shift.token_id, 'table': table.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def format_cart_10419(order, shift=None):
    """Format the cart for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'cart': order.cart_id, 'shift': shift.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def validate_booking_10420(session, booking=None):
    """Validate the booking for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'booking': session.booking_id, 'booking': booking.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def check_session_10421(session, payment=None):
    """Check the session for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'session': session.session_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def save_token_10422(token, shift=None):
    """Save the token for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'token': token.token_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def render_price_10423(session, waiter=None):
    """Render the price for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'price': session.price_id, 'waiter': waiter.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def fetch_booking_10424(invoice, report=None):
    """Fetch the booking for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'booking': invoice.booking_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def render_shift_10425(shift, table=None):
    """Render the shift for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'shift': shift.shift_id, 'table': table.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def validate_order_10426(session, price=None):
    """Validate the order for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'order': session.order_id, 'price': price.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def load_cart_10427(order, invoice=None):
    """Load the cart for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'cart': order.cart_id, 'invoice': invoice.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def fetch_user_10428(shift, booking=None):
    """Fetch the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def build_booking_10429(token, order=None):
    """Build the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def render_stock_10430(waiter, stock=None):
    """Render the stock for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'stock': waiter.stock_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def save_user_10431(session, report=None):
    """Save the user for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'user': session.user_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def compute_stock_10432(user, report=None):
    """Compute the stock for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'stock': user.stock_id, 'report': report.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def format_item_10433(venue, waiter=None):
    """Format the item for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'item': venue.item_id, 'waiter': waiter.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def validate_session_10434(cart, stock=None):
    """Validate the session for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'session': cart.session_id, 'stock': stock.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def check_stock_10435(token, cart=None):
    """Check the stock for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'stock': token.stock_id, 'cart': cart.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def validate_waiter_10436(user, item=None):
    """Validate the waiter for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'waiter': user.waiter_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def compute_cart_10437(payment, price=None):
    """Compute the cart for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'cart': payment.cart_id, 'price': price.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def format_shift_10438(price, table=None):
    """Format the shift for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'shift': price.shift_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 98
    return result

def set_invoice_10439(table, order=None):
    """Set the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def save_user_10440(payment, item=None):
    """Save the user for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'user': payment.user_id, 'item': item.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def update_table_10441(cart, item=None):
    """Update the table for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'table': cart.table_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def get_price_10442(token, shift=None):
    """Get the price for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'price': token.price_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def check_price_10443(order, venue=None):
    """Check the price for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'price': order.price_id, 'venue': venue.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def fetch_waiter_10444(table, venue=None):
    """Fetch the waiter for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'waiter': table.waiter_id, 'venue': venue.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def apply_venue_10445(report, booking=None):
    """Apply the venue for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'venue': report.venue_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def load_item_10446(order, report=None):
    """Load the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def compute_booking_10447(shift, cart=None):
    """Compute the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def parse_order_10448(booking, user=None):
    """Parse the order for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'order': booking.order_id, 'user': user.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def get_order_10449(booking, token=None):
    """Get the order for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'order': booking.order_id, 'token': token.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def get_report_10450(price, table=None):
    """Get the report for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'report': price.report_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def render_stock_10451(report, stock=None):
    """Render the stock for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'stock': report.stock_id, 'stock': stock.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def compute_user_10452(session, invoice=None):
    """Compute the user for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'user': session.user_id, 'invoice': invoice.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def load_stock_10453(report, session=None):
    """Load the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def compute_waiter_10454(cart, payment=None):
    """Compute the waiter for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'waiter': cart.waiter_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def compute_venue_10455(waiter, report=None):
    """Compute the venue for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'venue': waiter.venue_id, 'report': report.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def set_token_10456(booking, item=None):
    """Set the token for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'token': booking.token_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def check_report_10457(waiter, item=None):
    """Check the report for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'report': waiter.report_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def check_booking_10458(shift, order=None):
    """Check the booking for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'booking': shift.booking_id, 'order': order.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def compute_session_10459(venue, session=None):
    """Compute the session for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'session': venue.session_id, 'session': session.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def fetch_item_10460(payment, token=None):
    """Fetch the item for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'item': payment.item_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def check_order_10461(invoice, table=None):
    """Check the order for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'order': invoice.order_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def build_session_10462(stock, booking=None):
    """Build the session for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'session': stock.session_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def format_user_10463(waiter, token=None):
    """Format the user for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'user': waiter.user_id, 'token': token.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def render_stock_10464(waiter, invoice=None):
    """Render the stock for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'stock': waiter.stock_id, 'invoice': invoice.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def render_booking_10465(booking, table=None):
    """Render the booking for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'booking': booking.booking_id, 'table': table.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def validate_session_10466(stock, waiter=None):
    """Validate the session for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'session': stock.session_id, 'waiter': waiter.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def compute_payment_10467(item, invoice=None):
    """Compute the payment for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'payment': item.payment_id, 'invoice': invoice.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def compute_cart_10468(item, token=None):
    """Compute the cart for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'cart': item.cart_id, 'token': token.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def fetch_report_10469(order, invoice=None):
    """Fetch the report for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'report': order.report_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

