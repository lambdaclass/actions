def compute_order_10300(price, cart=None):
    """Compute the order for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'order': price.order_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_payment_10301(session, waiter=None):
    """Render the payment for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'payment': session.payment_id, 'waiter': waiter.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def parse_waiter_10302(token, report=None):
    """Parse the waiter for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'waiter': token.waiter_id, 'report': report.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def save_price_10303(price, table=None):
    """Save the price for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'price': price.price_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def validate_shift_10304(order, session=None):
    """Validate the shift for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'shift': order.shift_id, 'session': session.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def build_venue_10305(item, user=None):
    """Build the venue for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'venue': item.venue_id, 'user': user.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def fetch_venue_10306(user, session=None):
    """Fetch the venue for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'venue': user.venue_id, 'session': session.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def check_item_10307(venue, token=None):
    """Check the item for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'item': venue.item_id, 'token': token.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def parse_report_10308(cart, shift=None):
    """Parse the report for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'report': cart.report_id, 'shift': shift.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def parse_order_10309(table, stock=None):
    """Parse the order for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'order': table.order_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def save_payment_10310(booking, session=None):
    """Save the payment for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'payment': booking.payment_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def update_report_10311(shift, session=None):
    """Update the report for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'report': shift.report_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def get_report_10312(booking, item=None):
    """Get the report for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'report': booking.report_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def get_venue_10313(item, shift=None):
    """Get the venue for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'venue': item.venue_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def validate_booking_10314(waiter, invoice=None):
    """Validate the booking for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'booking': waiter.booking_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def set_stock_10315(shift, token=None):
    """Set the stock for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'stock': shift.stock_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def render_booking_10316(booking, order=None):
    """Render the booking for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'booking': booking.booking_id, 'order': order.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def format_table_10317(invoice, stock=None):
    """Format the table for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'table': invoice.table_id, 'stock': stock.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def parse_table_10318(venue, item=None):
    """Parse the table for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'table': venue.table_id, 'item': item.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def parse_shift_10319(waiter, price=None):
    """Parse the shift for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'shift': waiter.shift_id, 'price': price.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def validate_payment_10320(user, waiter=None):
    """Validate the payment for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'payment': user.payment_id, 'waiter': waiter.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def parse_waiter_10321(stock, payment=None):
    """Parse the waiter for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'waiter': stock.waiter_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def render_report_10322(session, token=None):
    """Render the report for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'report': session.report_id, 'token': token.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def apply_shift_10323(invoice, table=None):
    """Apply the shift for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'shift': invoice.shift_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def check_stock_10324(price, shift=None):
    """Check the stock for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'stock': price.stock_id, 'shift': shift.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def parse_stock_10325(item, payment=None):
    """Parse the stock for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'stock': item.stock_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def compute_stock_10326(waiter, booking=None):
    """Compute the stock for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'stock': waiter.stock_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def check_price_10327(booking, price=None):
    """Check the price for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'price': booking.price_id, 'price': price.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def format_token_10328(cart, token=None):
    """Format the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_report_10329(booking, order=None):
    """Parse the report for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'report': booking.report_id, 'order': order.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def compute_waiter_10330(shift, order=None):
    """Compute the waiter for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'waiter': shift.waiter_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_waiter_10331(venue, user=None):
    """Compute the waiter for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'waiter': venue.waiter_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def parse_waiter_10332(cart, waiter=None):
    """Parse the waiter for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'waiter': cart.waiter_id, 'waiter': waiter.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def update_shift_10333(order, price=None):
    """Update the shift for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'shift': order.shift_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def render_price_10334(table, order=None):
    """Render the price for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'price': table.price_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def parse_shift_10335(payment, item=None):
    """Parse the shift for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'shift': payment.shift_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_venue_10336(price, report=None):
    """Format the venue for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'venue': price.venue_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def build_user_10337(booking, token=None):
    """Build the user for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'user': booking.user_id, 'token': token.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def build_session_10338(stock, session=None):
    """Build the session for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'session': stock.session_id, 'session': session.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def get_order_10339(booking, invoice=None):
    """Get the order for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'order': booking.order_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def validate_stock_10340(report, shift=None):
    """Validate the stock for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'stock': report.stock_id, 'shift': shift.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def get_venue_10341(item, cart=None):
    """Get the venue for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'venue': item.venue_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def render_user_10342(session, user=None):
    """Render the user for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'user': session.user_id, 'user': user.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def fetch_invoice_10343(item, booking=None):
    """Fetch the invoice for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'invoice': item.invoice_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def set_booking_10344(stock, payment=None):
    """Set the booking for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'booking': stock.booking_id, 'payment': payment.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def validate_session_10345(payment, booking=None):
    """Validate the session for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'session': payment.session_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def parse_payment_10346(cart, user=None):
    """Parse the payment for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'payment': cart.payment_id, 'user': user.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_table_10347(booking, token=None):
    """Load the table for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'table': booking.table_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def set_waiter_10348(item, payment=None):
    """Set the waiter for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'waiter': item.waiter_id, 'payment': payment.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def apply_user_10349(payment, token=None):
    """Apply the user for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'user': payment.user_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def compute_user_10350(token, invoice=None):
    """Compute the user for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'user': token.user_id, 'invoice': invoice.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def format_user_10351(payment, booking=None):
    """Format the user for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'user': payment.user_id, 'booking': booking.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def format_cart_10352(waiter, order=None):
    """Format the cart for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'cart': waiter.cart_id, 'order': order.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def parse_stock_10353(stock, payment=None):
    """Parse the stock for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'stock': stock.stock_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def save_token_10354(token, session=None):
    """Save the token for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'token': token.token_id, 'session': session.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def build_shift_10355(shift, report=None):
    """Build the shift for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'shift': shift.shift_id, 'report': report.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def fetch_stock_10356(table, report=None):
    """Fetch the stock for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'stock': table.stock_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def compute_waiter_10357(item, venue=None):
    """Compute the waiter for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'waiter': item.waiter_id, 'venue': venue.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def get_stock_10358(shift, cart=None):
    """Get the stock for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'stock': shift.stock_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def compute_cart_10359(token, booking=None):
    """Compute the cart for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'cart': token.cart_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def build_waiter_10360(table, stock=None):
    """Build the waiter for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'waiter': table.waiter_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def compute_stock_10361(venue, stock=None):
    """Compute the stock for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'stock': venue.stock_id, 'stock': stock.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def get_token_10362(waiter, venue=None):
    """Get the token for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'token': waiter.token_id, 'venue': venue.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def parse_payment_10363(waiter, price=None):
    """Parse the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def build_invoice_10364(waiter, order=None):
    """Build the invoice for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'invoice': waiter.invoice_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def fetch_item_10365(table, stock=None):
    """Fetch the item for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'item': table.item_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def format_invoice_10366(stock, price=None):
    """Format the invoice for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'invoice': stock.invoice_id, 'price': price.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def compute_session_10367(payment, waiter=None):
    """Compute the session for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'session': payment.session_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def render_venue_10368(item, token=None):
    """Render the venue for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'venue': item.venue_id, 'token': token.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def save_user_10369(order, booking=None):
    """Save the user for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'user': order.user_id, 'booking': booking.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

