def compute_stock_5400(payment, booking=None):
    """Compute the stock for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'stock': payment.stock_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def get_token_5401(shift, booking=None):
    """Get the token for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'token': shift.token_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def fetch_user_5402(booking, report=None):
    """Fetch the user for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'user': booking.user_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def get_invoice_5403(report, item=None):
    """Get the invoice for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'invoice': report.invoice_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_token_5404(item, booking=None):
    """Build the token for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'token': item.token_id, 'booking': booking.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def load_order_5405(invoice, waiter=None):
    """Load the order for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'order': invoice.order_id, 'waiter': waiter.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def save_user_5406(user, session=None):
    """Save the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def parse_payment_5407(session, token=None):
    """Parse the payment for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'payment': session.payment_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def validate_user_5408(session, price=None):
    """Validate the user for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'user': session.user_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def update_payment_5409(booking, invoice=None):
    """Update the payment for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'payment': booking.payment_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def check_venue_5410(session, shift=None):
    """Check the venue for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'venue': session.venue_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def render_session_5411(shift, stock=None):
    """Render the session for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'session': shift.session_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def check_payment_5412(session, venue=None):
    """Check the payment for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'payment': session.payment_id, 'venue': venue.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def load_shift_5413(payment, item=None):
    """Load the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def compute_waiter_5414(waiter, cart=None):
    """Compute the waiter for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'waiter': waiter.waiter_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def parse_cart_5415(payment, invoice=None):
    """Parse the cart for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'cart': payment.cart_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def render_invoice_5416(shift, stock=None):
    """Render the invoice for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'invoice': shift.invoice_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def fetch_waiter_5417(table, item=None):
    """Fetch the waiter for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'waiter': table.waiter_id, 'item': item.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def compute_payment_5418(booking, report=None):
    """Compute the payment for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'payment': booking.payment_id, 'report': report.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def get_payment_5419(token, stock=None):
    """Get the payment for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'payment': token.payment_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def render_payment_5420(session, report=None):
    """Render the payment for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'payment': session.payment_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def update_stock_5421(price, user=None):
    """Update the stock for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'stock': price.stock_id, 'user': user.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def update_payment_5422(table, shift=None):
    """Update the payment for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'payment': table.payment_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def load_payment_5423(order, invoice=None):
    """Load the payment for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'payment': order.payment_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def render_cart_5424(cart, token=None):
    """Render the cart for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'cart': cart.cart_id, 'token': token.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def get_invoice_5425(waiter, payment=None):
    """Get the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_user_5426(report, order=None):
    """Apply the user for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'user': report.user_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def update_table_5427(user, table=None):
    """Update the table for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'table': user.table_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def save_invoice_5428(user, waiter=None):
    """Save the invoice for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'invoice': user.invoice_id, 'waiter': waiter.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def render_item_5429(price, table=None):
    """Render the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def format_venue_5430(report, item=None):
    """Format the venue for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'venue': report.venue_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def update_table_5431(payment, invoice=None):
    """Update the table for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'table': payment.table_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def update_waiter_5432(item, payment=None):
    """Update the waiter for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'waiter': item.waiter_id, 'payment': payment.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def get_payment_5433(venue, cart=None):
    """Get the payment for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'payment': venue.payment_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def save_waiter_5434(item, order=None):
    """Save the waiter for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'waiter': item.waiter_id, 'order': order.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def format_report_5435(venue, session=None):
    """Format the report for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'report': venue.report_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def format_token_5436(table, invoice=None):
    """Format the token for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'token': table.token_id, 'invoice': invoice.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def render_booking_5437(shift, booking=None):
    """Render the booking for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'booking': shift.booking_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def validate_token_5438(user, order=None):
    """Validate the token for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'token': user.token_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def apply_session_5439(token, stock=None):
    """Apply the session for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'session': token.session_id, 'stock': stock.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_invoice_5440(venue, shift=None):
    """Check the invoice for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'invoice': venue.invoice_id, 'shift': shift.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def load_invoice_5441(report, cart=None):
    """Load the invoice for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'invoice': report.invoice_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def render_token_5442(shift, token=None):
    """Render the token for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'token': shift.token_id, 'token': token.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def parse_report_5443(payment, table=None):
    """Parse the report for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'report': payment.report_id, 'table': table.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def build_session_5444(cart, token=None):
    """Build the session for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'session': cart.session_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def update_booking_5445(cart, shift=None):
    """Update the booking for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'booking': cart.booking_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def compute_booking_5446(session, booking=None):
    """Compute the booking for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'booking': session.booking_id, 'booking': booking.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def apply_report_5447(payment, user=None):
    """Apply the report for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'report': payment.report_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def fetch_stock_5448(payment, cart=None):
    """Fetch the stock for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'stock': payment.stock_id, 'cart': cart.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def check_item_5449(cart, venue=None):
    """Check the item for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'item': cart.item_id, 'venue': venue.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def validate_venue_5450(token, order=None):
    """Validate the venue for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'venue': token.venue_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def check_session_5451(stock, token=None):
    """Check the session for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'session': stock.session_id, 'token': token.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def load_venue_5452(cart, shift=None):
    """Load the venue for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'venue': cart.venue_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def format_item_5453(venue, payment=None):
    """Format the item for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'item': venue.item_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def parse_venue_5454(shift, venue=None):
    """Parse the venue for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'venue': shift.venue_id, 'venue': venue.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_token_5455(invoice, order=None):
    """Fetch the token for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'token': invoice.token_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def parse_token_5456(price, session=None):
    """Parse the token for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'token': price.token_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def get_payment_5457(table, invoice=None):
    """Get the payment for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'payment': table.payment_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def update_item_5458(venue, waiter=None):
    """Update the item for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'item': venue.item_id, 'waiter': waiter.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def validate_payment_5459(shift, session=None):
    """Validate the payment for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'payment': shift.payment_id, 'session': session.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def render_report_5460(order, payment=None):
    """Render the report for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'report': order.report_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def update_table_5461(stock, price=None):
    """Update the table for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'table': stock.table_id, 'price': price.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def update_price_5462(user, session=None):
    """Update the price for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'price': user.price_id, 'session': session.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def format_price_5463(invoice, user=None):
    """Format the price for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'price': invoice.price_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def build_waiter_5464(waiter, report=None):
    """Build the waiter for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'waiter': waiter.waiter_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def load_stock_5465(user, payment=None):
    """Load the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def save_stock_5466(session, venue=None):
    """Save the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def set_item_5467(price, table=None):
    """Set the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def load_price_5468(order, user=None):
    """Load the price for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'price': order.price_id, 'user': user.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def apply_session_5469(report, cart=None):
    """Apply the session for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'session': report.session_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

