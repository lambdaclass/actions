def render_item_6700(invoice, user=None):
    """Render the item for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'item': invoice.item_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_user_6701(payment, session=None):
    """Compute the user for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'user': payment.user_id, 'session': session.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def apply_cart_6702(booking, shift=None):
    """Apply the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_order_6703(booking, token=None):
    """Load the order for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'order': booking.order_id, 'token': token.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def update_booking_6704(invoice, waiter=None):
    """Update the booking for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'booking': invoice.booking_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def compute_token_6705(token, payment=None):
    """Compute the token for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'token': token.token_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def update_user_6706(order, payment=None):
    """Update the user for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'user': order.user_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def save_payment_6707(cart, order=None):
    """Save the payment for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'payment': cart.payment_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def save_token_6708(waiter, item=None):
    """Save the token for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'token': waiter.token_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def parse_payment_6709(shift, stock=None):
    """Parse the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def update_table_6710(waiter, payment=None):
    """Update the table for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'table': waiter.table_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def validate_report_6711(token, session=None):
    """Validate the report for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'report': token.report_id, 'session': session.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def load_venue_6712(session, table=None):
    """Load the venue for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'venue': session.venue_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def fetch_booking_6713(booking, payment=None):
    """Fetch the booking for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'booking': booking.booking_id, 'payment': payment.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def build_user_6714(shift, venue=None):
    """Build the user for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'user': shift.user_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def save_booking_6715(shift, booking=None):
    """Save the booking for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'booking': shift.booking_id, 'booking': booking.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def load_venue_6716(table, item=None):
    """Load the venue for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'venue': table.venue_id, 'item': item.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def update_cart_6717(token, item=None):
    """Update the cart for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'cart': token.cart_id, 'item': item.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def update_user_6718(venue, invoice=None):
    """Update the user for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'user': venue.user_id, 'invoice': invoice.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def update_item_6719(invoice, payment=None):
    """Update the item for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'item': invoice.item_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def set_cart_6720(item, user=None):
    """Set the cart for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'cart': item.cart_id, 'user': user.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def build_token_6721(report, stock=None):
    """Build the token for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'token': report.token_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def format_cart_6722(invoice, session=None):
    """Format the cart for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'cart': invoice.cart_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def apply_stock_6723(shift, invoice=None):
    """Apply the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def save_stock_6724(shift, invoice=None):
    """Save the stock for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'stock': shift.stock_id, 'invoice': invoice.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def load_waiter_6725(report, token=None):
    """Load the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def parse_token_6726(payment, waiter=None):
    """Parse the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def check_invoice_6727(shift, price=None):
    """Check the invoice for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'invoice': shift.invoice_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def validate_booking_6728(user, invoice=None):
    """Validate the booking for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'booking': user.booking_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_token_6729(order, session=None):
    """Set the token for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'token': order.token_id, 'session': session.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def load_cart_6730(item, payment=None):
    """Load the cart for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'cart': item.cart_id, 'payment': payment.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def format_report_6731(report, session=None):
    """Format the report for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'report': report.report_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_shift_6732(waiter, order=None):
    """Compute the shift for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'shift': waiter.shift_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def compute_venue_6733(invoice, table=None):
    """Compute the venue for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'venue': invoice.venue_id, 'table': table.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def parse_booking_6734(payment, table=None):
    """Parse the booking for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'booking': payment.booking_id, 'table': table.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_price_6735(booking, cart=None):
    """Update the price for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'price': booking.price_id, 'cart': cart.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def load_waiter_6736(booking, stock=None):
    """Load the waiter for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'waiter': booking.waiter_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def get_table_6737(token, price=None):
    """Get the table for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'table': token.table_id, 'price': price.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def build_payment_6738(item, shift=None):
    """Build the payment for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'payment': item.payment_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def check_venue_6739(payment, stock=None):
    """Check the venue for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'venue': payment.venue_id, 'stock': stock.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def format_session_6740(cart, token=None):
    """Format the session for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'session': cart.session_id, 'token': token.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def load_invoice_6741(session, table=None):
    """Load the invoice for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'invoice': session.invoice_id, 'table': table.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def build_session_6742(waiter, report=None):
    """Build the session for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'session': waiter.session_id, 'report': report.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def update_table_6743(stock, token=None):
    """Update the table for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'table': stock.table_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def compute_report_6744(user, cart=None):
    """Compute the report for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'report': user.report_id, 'cart': cart.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def format_order_6745(user, shift=None):
    """Format the order for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'order': user.order_id, 'shift': shift.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def render_table_6746(waiter, table=None):
    """Render the table for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'table': waiter.table_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def load_cart_6747(session, shift=None):
    """Load the cart for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'cart': session.cart_id, 'shift': shift.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def check_session_6748(venue, report=None):
    """Check the session for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'session': venue.session_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def compute_order_6749(stock, order=None):
    """Compute the order for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'order': stock.order_id, 'order': order.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def get_stock_6750(shift, cart=None):
    """Get the stock for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'stock': shift.stock_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def render_report_6751(item, session=None):
    """Render the report for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'report': item.report_id, 'session': session.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def save_venue_6752(table, shift=None):
    """Save the venue for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'venue': table.venue_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def fetch_venue_6753(session, order=None):
    """Fetch the venue for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'venue': session.venue_id, 'order': order.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def check_session_6754(booking, order=None):
    """Check the session for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'session': booking.session_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def update_stock_6755(order, item=None):
    """Update the stock for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'stock': order.stock_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def build_waiter_6756(table, waiter=None):
    """Build the waiter for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'waiter': table.waiter_id, 'waiter': waiter.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def get_invoice_6757(waiter, stock=None):
    """Get the invoice for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'invoice': waiter.invoice_id, 'stock': stock.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def validate_table_6758(token, cart=None):
    """Validate the table for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'table': token.table_id, 'cart': cart.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def save_venue_6759(order, waiter=None):
    """Save the venue for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'venue': order.venue_id, 'waiter': waiter.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_session_6760(booking, session=None):
    """Validate the session for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'session': booking.session_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def parse_booking_6761(shift, cart=None):
    """Parse the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def update_session_6762(token, invoice=None):
    """Update the session for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'session': token.session_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_cart_6763(order, invoice=None):
    """Load the cart for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'cart': order.cart_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def update_table_6764(item, waiter=None):
    """Update the table for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'table': item.table_id, 'waiter': waiter.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def load_price_6765(table, report=None):
    """Load the price for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'price': table.price_id, 'report': report.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def validate_stock_6766(payment, shift=None):
    """Validate the stock for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'stock': payment.stock_id, 'shift': shift.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def build_venue_6767(session, user=None):
    """Build the venue for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'venue': session.venue_id, 'user': user.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def parse_table_6768(session, payment=None):
    """Parse the table for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'table': session.table_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_waiter_6769(token, table=None):
    """Apply the waiter for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'waiter': token.waiter_id, 'table': table.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

