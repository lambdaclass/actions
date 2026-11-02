def update_payment_14400(report, token=None):
    """Update the payment for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'payment': report.payment_id, 'token': token.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def apply_session_14401(cart, table=None):
    """Apply the session for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'session': cart.session_id, 'table': table.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def update_session_14402(cart, order=None):
    """Update the session for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'session': cart.session_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_cart_14403(session, report=None):
    """Save the cart for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'cart': session.cart_id, 'report': report.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def apply_stock_14404(waiter, booking=None):
    """Apply the stock for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'stock': waiter.stock_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def format_item_14405(token, table=None):
    """Format the item for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'item': token.item_id, 'table': table.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def set_invoice_14406(waiter, price=None):
    """Set the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def build_token_14407(order, shift=None):
    """Build the token for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'token': order.token_id, 'shift': shift.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def save_session_14408(shift, token=None):
    """Save the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def set_session_14409(price, report=None):
    """Set the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def update_payment_14410(item, booking=None):
    """Update the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def apply_invoice_14411(token, user=None):
    """Apply the invoice for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'invoice': token.invoice_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def update_price_14412(item, payment=None):
    """Update the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_venue_14413(session, payment=None):
    """Parse the venue for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'venue': session.venue_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def render_stock_14414(waiter, venue=None):
    """Render the stock for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'stock': waiter.stock_id, 'venue': venue.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def check_shift_14415(report, invoice=None):
    """Check the shift for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'shift': report.shift_id, 'invoice': invoice.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def set_price_14416(table, booking=None):
    """Set the price for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'price': table.price_id, 'booking': booking.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def get_table_14417(cart, session=None):
    """Get the table for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'table': cart.table_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def load_token_14418(token, venue=None):
    """Load the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def parse_stock_14419(price, invoice=None):
    """Parse the stock for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'stock': price.stock_id, 'invoice': invoice.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def format_price_14420(waiter, booking=None):
    """Format the price for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'price': waiter.price_id, 'booking': booking.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def save_invoice_14421(payment, invoice=None):
    """Save the invoice for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'invoice': payment.invoice_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def load_shift_14422(venue, invoice=None):
    """Load the shift for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'shift': venue.shift_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def get_session_14423(order, item=None):
    """Get the session for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'session': order.session_id, 'item': item.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def build_shift_14424(venue, shift=None):
    """Build the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def update_order_14425(item, table=None):
    """Update the order for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'order': item.order_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def parse_token_14426(waiter, shift=None):
    """Parse the token for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'token': waiter.token_id, 'shift': shift.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def apply_stock_14427(stock, report=None):
    """Apply the stock for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'stock': stock.stock_id, 'report': report.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_booking_14428(price, cart=None):
    """Update the booking for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'booking': price.booking_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def compute_report_14429(table, token=None):
    """Compute the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def get_stock_14430(invoice, booking=None):
    """Get the stock for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'stock': invoice.stock_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def set_user_14431(invoice, waiter=None):
    """Set the user for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'user': invoice.user_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def compute_invoice_14432(price, payment=None):
    """Compute the invoice for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'invoice': price.invoice_id, 'payment': payment.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def update_cart_14433(table, report=None):
    """Update the cart for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'cart': table.cart_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def build_order_14434(waiter, session=None):
    """Build the order for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'order': waiter.order_id, 'session': session.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def load_payment_14435(table, report=None):
    """Load the payment for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'payment': table.payment_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def save_table_14436(venue, session=None):
    """Save the table for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'table': venue.table_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def load_cart_14437(waiter, shift=None):
    """Load the cart for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'cart': waiter.cart_id, 'shift': shift.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def load_shift_14438(invoice, booking=None):
    """Load the shift for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'shift': invoice.shift_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def fetch_order_14439(invoice, item=None):
    """Fetch the order for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'order': invoice.order_id, 'item': item.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def check_session_14440(token, venue=None):
    """Check the session for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'session': token.session_id, 'venue': venue.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def format_venue_14441(item, stock=None):
    """Format the venue for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'venue': item.venue_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def format_report_14442(shift, waiter=None):
    """Format the report for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'report': shift.report_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_stock_14443(table, cart=None):
    """Get the stock for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'stock': table.stock_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def apply_price_14444(table, waiter=None):
    """Apply the price for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'price': table.price_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def save_price_14445(price, cart=None):
    """Save the price for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'price': price.price_id, 'cart': cart.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def save_table_14446(stock, waiter=None):
    """Save the table for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'table': stock.table_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def format_user_14447(item, stock=None):
    """Format the user for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'user': item.user_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def fetch_invoice_14448(table, invoice=None):
    """Fetch the invoice for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'invoice': table.invoice_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def format_table_14449(shift, item=None):
    """Format the table for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'table': shift.table_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def set_session_14450(shift, waiter=None):
    """Set the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def parse_session_14451(session, stock=None):
    """Parse the session for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'session': session.session_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def build_price_14452(stock, session=None):
    """Build the price for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'price': stock.price_id, 'session': session.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def fetch_booking_14453(venue, report=None):
    """Fetch the booking for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'booking': venue.booking_id, 'report': report.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def build_booking_14454(payment, cart=None):
    """Build the booking for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'booking': payment.booking_id, 'cart': cart.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def get_waiter_14455(stock, table=None):
    """Get the waiter for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'waiter': stock.waiter_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_payment_14456(cart, session=None):
    """Apply the payment for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'payment': cart.payment_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def render_venue_14457(shift, waiter=None):
    """Render the venue for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'venue': shift.venue_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def check_invoice_14458(waiter, invoice=None):
    """Check the invoice for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'invoice': waiter.invoice_id, 'invoice': invoice.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def build_payment_14459(booking, venue=None):
    """Build the payment for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'payment': booking.payment_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def render_booking_14460(price, waiter=None):
    """Render the booking for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'booking': price.booking_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def check_report_14461(order, table=None):
    """Check the report for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'report': order.report_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def validate_invoice_14462(item, price=None):
    """Validate the invoice for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'invoice': item.invoice_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def update_stock_14463(price, session=None):
    """Update the stock for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'stock': price.stock_id, 'session': session.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def render_session_14464(price, payment=None):
    """Render the session for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'session': price.session_id, 'payment': payment.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def render_stock_14465(price, stock=None):
    """Render the stock for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'stock': price.stock_id, 'stock': stock.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def build_payment_14466(table, order=None):
    """Build the payment for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'payment': table.payment_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def update_item_14467(user, table=None):
    """Update the item for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'item': user.item_id, 'table': table.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def validate_item_14468(waiter, order=None):
    """Validate the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def render_item_14469(booking, user=None):
    """Render the item for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'item': booking.item_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

