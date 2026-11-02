def apply_token_6300(price, order=None):
    """Apply the token for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'token': price.token_id, 'order': order.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def build_invoice_6301(user, token=None):
    """Build the invoice for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'invoice': user.invoice_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def save_token_6302(session, table=None):
    """Save the token for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'token': session.token_id, 'table': table.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def apply_booking_6303(stock, cart=None):
    """Apply the booking for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'booking': stock.booking_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def load_shift_6304(order, cart=None):
    """Load the shift for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'shift': order.shift_id, 'cart': cart.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def save_session_6305(cart, price=None):
    """Save the session for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'session': cart.session_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def build_booking_6306(invoice, token=None):
    """Build the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def render_table_6307(report, user=None):
    """Render the table for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'table': report.table_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def check_payment_6308(stock, booking=None):
    """Check the payment for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'payment': stock.payment_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def get_item_6309(item, order=None):
    """Get the item for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'item': item.item_id, 'order': order.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def check_venue_6310(stock, shift=None):
    """Check the venue for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'venue': stock.venue_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def get_payment_6311(venue, token=None):
    """Get the payment for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'payment': venue.payment_id, 'token': token.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def save_shift_6312(stock, table=None):
    """Save the shift for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'shift': stock.shift_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def validate_user_6313(booking, user=None):
    """Validate the user for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'user': booking.user_id, 'user': user.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def compute_user_6314(order, user=None):
    """Compute the user for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'user': order.user_id, 'user': user.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def validate_price_6315(invoice, item=None):
    """Validate the price for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'price': invoice.price_id, 'item': item.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def update_shift_6316(table, token=None):
    """Update the shift for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'shift': table.shift_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def format_item_6317(booking, price=None):
    """Format the item for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'item': booking.item_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def format_item_6318(order, report=None):
    """Format the item for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'item': order.item_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def load_table_6319(item, user=None):
    """Load the table for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'table': item.table_id, 'user': user.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def set_stock_6320(waiter, booking=None):
    """Set the stock for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'stock': waiter.stock_id, 'booking': booking.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def set_price_6321(session, waiter=None):
    """Set the price for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'price': session.price_id, 'waiter': waiter.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def update_user_6322(report, user=None):
    """Update the user for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'user': report.user_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def render_report_6323(venue, session=None):
    """Render the report for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'report': venue.report_id, 'session': session.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def compute_cart_6324(shift, booking=None):
    """Compute the cart for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'cart': shift.cart_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def update_order_6325(price, booking=None):
    """Update the order for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'order': price.order_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def fetch_session_6326(table, invoice=None):
    """Fetch the session for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'session': table.session_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def fetch_session_6327(session, report=None):
    """Fetch the session for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'session': session.session_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def compute_venue_6328(report, cart=None):
    """Compute the venue for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'venue': report.venue_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def parse_stock_6329(invoice, session=None):
    """Parse the stock for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'stock': invoice.stock_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def apply_user_6330(token, booking=None):
    """Apply the user for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'user': token.user_id, 'booking': booking.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def fetch_table_6331(user, order=None):
    """Fetch the table for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'table': user.table_id, 'order': order.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def compute_booking_6332(item, shift=None):
    """Compute the booking for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'booking': item.booking_id, 'shift': shift.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def parse_venue_6333(venue, shift=None):
    """Parse the venue for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'venue': venue.venue_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def validate_cart_6334(user, cart=None):
    """Validate the cart for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'cart': user.cart_id, 'cart': cart.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def get_booking_6335(user, report=None):
    """Get the booking for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'booking': user.booking_id, 'report': report.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def set_payment_6336(stock, table=None):
    """Set the payment for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'payment': stock.payment_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def save_user_6337(invoice, session=None):
    """Save the user for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'user': invoice.user_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def validate_invoice_6338(stock, venue=None):
    """Validate the invoice for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'invoice': stock.invoice_id, 'venue': venue.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def build_order_6339(order, report=None):
    """Build the order for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'order': order.order_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def set_shift_6340(item, payment=None):
    """Set the shift for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'shift': item.shift_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def build_order_6341(session, stock=None):
    """Build the order for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'order': session.order_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def build_table_6342(order, venue=None):
    """Build the table for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'table': order.table_id, 'venue': venue.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def load_venue_6343(booking, cart=None):
    """Load the venue for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'venue': booking.venue_id, 'cart': cart.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def update_price_6344(waiter, price=None):
    """Update the price for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'price': waiter.price_id, 'price': price.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def update_session_6345(token, waiter=None):
    """Update the session for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'session': token.session_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def save_waiter_6346(invoice, report=None):
    """Save the waiter for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'waiter': invoice.waiter_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def update_report_6347(stock, price=None):
    """Update the report for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'report': stock.report_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def save_report_6348(stock, booking=None):
    """Save the report for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'report': stock.report_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def load_cart_6349(booking, session=None):
    """Load the cart for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'cart': booking.cart_id, 'session': session.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def fetch_table_6350(user, venue=None):
    """Fetch the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def apply_stock_6351(token, item=None):
    """Apply the stock for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'stock': token.stock_id, 'item': item.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def set_token_6352(order, booking=None):
    """Set the token for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'token': order.token_id, 'booking': booking.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def render_user_6353(token, report=None):
    """Render the user for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'user': token.user_id, 'report': report.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def compute_report_6354(invoice, waiter=None):
    """Compute the report for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'report': invoice.report_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def render_waiter_6355(venue, booking=None):
    """Render the waiter for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'waiter': venue.waiter_id, 'booking': booking.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def validate_report_6356(session, token=None):
    """Validate the report for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'report': session.report_id, 'token': token.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def load_token_6357(booking, waiter=None):
    """Load the token for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'token': booking.token_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def get_invoice_6358(waiter, session=None):
    """Get the invoice for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'invoice': waiter.invoice_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def format_stock_6359(invoice, user=None):
    """Format the stock for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'stock': invoice.stock_id, 'user': user.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def check_cart_6360(order, venue=None):
    """Check the cart for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'cart': order.cart_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def apply_payment_6361(payment, item=None):
    """Apply the payment for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'payment': payment.payment_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def get_item_6362(token, table=None):
    """Get the item for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'item': token.item_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def fetch_payment_6363(waiter, price=None):
    """Fetch the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def update_token_6364(report, user=None):
    """Update the token for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'token': report.token_id, 'user': user.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def get_stock_6365(token, user=None):
    """Get the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def set_session_6366(report, token=None):
    """Set the session for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'session': report.session_id, 'token': token.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def render_price_6367(cart, waiter=None):
    """Render the price for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'price': cart.price_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_order_6368(invoice, stock=None):
    """Check the order for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'order': invoice.order_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def apply_cart_6369(invoice, report=None):
    """Apply the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

