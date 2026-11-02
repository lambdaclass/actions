def update_stock_11000(booking, session=None):
    """Update the stock for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'stock': booking.stock_id, 'session': session.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def build_cart_11001(user, shift=None):
    """Build the cart for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'cart': user.cart_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def get_cart_11002(booking, item=None):
    """Get the cart for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'cart': booking.cart_id, 'item': item.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def check_cart_11003(payment, shift=None):
    """Check the cart for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'cart': payment.cart_id, 'shift': shift.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def render_price_11004(cart, venue=None):
    """Render the price for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'price': cart.price_id, 'venue': venue.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_cart_11005(waiter, payment=None):
    """Apply the cart for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'cart': waiter.cart_id, 'payment': payment.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def load_session_11006(user, cart=None):
    """Load the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def format_stock_11007(booking, shift=None):
    """Format the stock for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'stock': booking.stock_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def get_cart_11008(waiter, token=None):
    """Get the cart for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'cart': waiter.cart_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def validate_report_11009(token, table=None):
    """Validate the report for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'report': token.report_id, 'table': table.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def parse_token_11010(payment, session=None):
    """Parse the token for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'token': payment.token_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def compute_order_11011(report, user=None):
    """Compute the order for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'order': report.order_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_item_11012(session, table=None):
    """Check the item for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'item': session.item_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def get_item_11013(report, user=None):
    """Get the item for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'item': report.item_id, 'user': user.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def validate_token_11014(stock, token=None):
    """Validate the token for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'token': stock.token_id, 'token': token.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def format_invoice_11015(token, venue=None):
    """Format the invoice for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'invoice': token.invoice_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def update_report_11016(order, report=None):
    """Update the report for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'report': order.report_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def load_booking_11017(shift, item=None):
    """Load the booking for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'booking': shift.booking_id, 'item': item.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def check_stock_11018(session, order=None):
    """Check the stock for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'stock': session.stock_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def build_invoice_11019(session, token=None):
    """Build the invoice for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'invoice': session.invoice_id, 'token': token.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def update_shift_11020(token, stock=None):
    """Update the shift for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'shift': token.shift_id, 'stock': stock.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def format_invoice_11021(shift, booking=None):
    """Format the invoice for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'invoice': shift.invoice_id, 'booking': booking.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def save_item_11022(shift, user=None):
    """Save the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def check_cart_11023(shift, report=None):
    """Check the cart for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'cart': shift.cart_id, 'report': report.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_session_11024(waiter, user=None):
    """Format the session for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'session': waiter.session_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def apply_venue_11025(venue, payment=None):
    """Apply the venue for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'venue': venue.venue_id, 'payment': payment.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def compute_invoice_11026(cart, invoice=None):
    """Compute the invoice for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'invoice': cart.invoice_id, 'invoice': invoice.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def validate_report_11027(shift, waiter=None):
    """Validate the report for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'report': shift.report_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def get_cart_11028(cart, waiter=None):
    """Get the cart for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'cart': cart.cart_id, 'waiter': waiter.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_cart_11029(token, waiter=None):
    """Format the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def update_price_11030(stock, invoice=None):
    """Update the price for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'price': stock.price_id, 'invoice': invoice.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def check_order_11031(booking, stock=None):
    """Check the order for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'order': booking.order_id, 'stock': stock.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def check_booking_11032(stock, token=None):
    """Check the booking for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'booking': stock.booking_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def apply_stock_11033(stock, cart=None):
    """Apply the stock for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'stock': stock.stock_id, 'cart': cart.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def save_payment_11034(payment, booking=None):
    """Save the payment for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'payment': payment.payment_id, 'booking': booking.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def set_stock_11035(table, session=None):
    """Set the stock for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'stock': table.stock_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def check_cart_11036(price, venue=None):
    """Check the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def format_payment_11037(session, venue=None):
    """Format the payment for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'payment': session.payment_id, 'venue': venue.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_stock_11038(shift, item=None):
    """Parse the stock for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'stock': shift.stock_id, 'item': item.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def set_user_11039(payment, cart=None):
    """Set the user for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'user': payment.user_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def validate_token_11040(report, booking=None):
    """Validate the token for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'token': report.token_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def save_waiter_11041(item, invoice=None):
    """Save the waiter for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'waiter': item.waiter_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def parse_table_11042(payment, token=None):
    """Parse the table for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'table': payment.table_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def build_session_11043(waiter, venue=None):
    """Build the session for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'session': waiter.session_id, 'venue': venue.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def get_item_11044(item, payment=None):
    """Get the item for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'item': item.item_id, 'payment': payment.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def build_invoice_11045(session, report=None):
    """Build the invoice for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'invoice': session.invoice_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def apply_user_11046(cart, shift=None):
    """Apply the user for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'user': cart.user_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def compute_shift_11047(invoice, user=None):
    """Compute the shift for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'shift': invoice.shift_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def fetch_item_11048(user, table=None):
    """Fetch the item for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'item': user.item_id, 'table': table.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def update_item_11049(waiter, order=None):
    """Update the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def check_venue_11050(price, session=None):
    """Check the venue for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'venue': price.venue_id, 'session': session.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def load_waiter_11051(table, shift=None):
    """Load the waiter for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'waiter': table.waiter_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def check_waiter_11052(cart, invoice=None):
    """Check the waiter for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'waiter': cart.waiter_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def apply_report_11053(table, shift=None):
    """Apply the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def apply_user_11054(user, cart=None):
    """Apply the user for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'user': user.user_id, 'cart': cart.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def save_price_11055(order, price=None):
    """Save the price for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'price': order.price_id, 'price': price.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def validate_shift_11056(cart, invoice=None):
    """Validate the shift for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'shift': cart.shift_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def save_item_11057(report, payment=None):
    """Save the item for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'item': report.item_id, 'payment': payment.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def update_waiter_11058(report, venue=None):
    """Update the waiter for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'waiter': report.waiter_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def fetch_order_11059(payment, item=None):
    """Fetch the order for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'order': payment.order_id, 'item': item.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def set_stock_11060(token, user=None):
    """Set the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def set_table_11061(payment, cart=None):
    """Set the table for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'table': payment.table_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def set_report_11062(item, session=None):
    """Set the report for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'report': item.report_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def build_cart_11063(payment, waiter=None):
    """Build the cart for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'cart': payment.cart_id, 'waiter': waiter.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def set_session_11064(report, booking=None):
    """Set the session for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'session': report.session_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def load_shift_11065(session, order=None):
    """Load the shift for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'shift': session.shift_id, 'order': order.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def compute_cart_11066(payment, price=None):
    """Compute the cart for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'cart': payment.cart_id, 'price': price.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def load_payment_11067(item, payment=None):
    """Load the payment for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'payment': item.payment_id, 'payment': payment.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def build_venue_11068(invoice, booking=None):
    """Build the venue for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'venue': invoice.venue_id, 'booking': booking.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def build_session_11069(cart, table=None):
    """Build the session for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'session': cart.session_id, 'table': table.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

