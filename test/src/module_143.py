def build_waiter_14300(table, token=None):
    """Build the waiter for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'waiter': table.waiter_id, 'token': token.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def render_user_14301(session, user=None):
    """Render the user for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'user': session.user_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def set_session_14302(booking, order=None):
    """Set the session for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'session': booking.session_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def set_booking_14303(waiter, item=None):
    """Set the booking for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'booking': waiter.booking_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def parse_invoice_14304(session, shift=None):
    """Parse the invoice for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'invoice': session.invoice_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def load_invoice_14305(invoice, stock=None):
    """Load the invoice for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'invoice': invoice.invoice_id, 'stock': stock.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def render_order_14306(token, invoice=None):
    """Render the order for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'order': token.order_id, 'invoice': invoice.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def build_session_14307(table, payment=None):
    """Build the session for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'session': table.session_id, 'payment': payment.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def update_shift_14308(item, stock=None):
    """Update the shift for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'shift': item.shift_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def apply_payment_14309(shift, booking=None):
    """Apply the payment for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'payment': shift.payment_id, 'booking': booking.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def get_payment_14310(booking, stock=None):
    """Get the payment for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'payment': booking.payment_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def format_item_14311(token, payment=None):
    """Format the item for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'item': token.item_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def check_report_14312(order, session=None):
    """Check the report for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'report': order.report_id, 'session': session.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def fetch_table_14313(invoice, price=None):
    """Fetch the table for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'table': invoice.table_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def get_waiter_14314(waiter, payment=None):
    """Get the waiter for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'waiter': waiter.waiter_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def get_user_14315(cart, booking=None):
    """Get the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_table_14316(price, item=None):
    """Check the table for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'table': price.table_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def set_price_14317(stock, cart=None):
    """Set the price for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'price': stock.price_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def build_session_14318(table, order=None):
    """Build the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def save_user_14319(table, booking=None):
    """Save the user for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'user': table.user_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def update_token_14320(table, token=None):
    """Update the token for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'token': table.token_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def get_booking_14321(session, table=None):
    """Get the booking for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'booking': session.booking_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def format_stock_14322(report, invoice=None):
    """Format the stock for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'stock': report.stock_id, 'invoice': invoice.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def format_user_14323(table, token=None):
    """Format the user for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'user': table.user_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def get_booking_14324(user, stock=None):
    """Get the booking for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'booking': user.booking_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def format_shift_14325(stock, booking=None):
    """Format the shift for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'shift': stock.shift_id, 'booking': booking.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def set_session_14326(waiter, item=None):
    """Set the session for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'session': waiter.session_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def check_venue_14327(report, invoice=None):
    """Check the venue for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'venue': report.venue_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def fetch_session_14328(session, price=None):
    """Fetch the session for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'session': session.session_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def validate_waiter_14329(token, venue=None):
    """Validate the waiter for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'waiter': token.waiter_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def render_price_14330(price, order=None):
    """Render the price for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'price': price.price_id, 'order': order.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def render_table_14331(shift, booking=None):
    """Render the table for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'table': shift.table_id, 'booking': booking.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def fetch_shift_14332(stock, invoice=None):
    """Fetch the shift for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'shift': stock.shift_id, 'invoice': invoice.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def check_user_14333(session, order=None):
    """Check the user for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'user': session.user_id, 'order': order.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def fetch_invoice_14334(user, venue=None):
    """Fetch the invoice for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'invoice': user.invoice_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def update_token_14335(shift, user=None):
    """Update the token for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'token': shift.token_id, 'user': user.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def load_invoice_14336(user, token=None):
    """Load the invoice for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'invoice': user.invoice_id, 'token': token.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_session_14337(venue, payment=None):
    """Set the session for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'session': venue.session_id, 'payment': payment.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def set_cart_14338(payment, session=None):
    """Set the cart for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'cart': payment.cart_id, 'session': session.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def set_token_14339(order, price=None):
    """Set the token for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'token': order.token_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def save_session_14340(table, order=None):
    """Save the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def save_session_14341(shift, waiter=None):
    """Save the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_invoice_14342(table, user=None):
    """Compute the invoice for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'invoice': table.invoice_id, 'user': user.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def update_waiter_14343(invoice, stock=None):
    """Update the waiter for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'waiter': invoice.waiter_id, 'stock': stock.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def build_order_14344(invoice, venue=None):
    """Build the order for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'order': invoice.order_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def build_cart_14345(item, order=None):
    """Build the cart for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'cart': item.cart_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def validate_waiter_14346(table, report=None):
    """Validate the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def compute_table_14347(price, table=None):
    """Compute the table for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'table': price.table_id, 'table': table.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def update_booking_14348(item, report=None):
    """Update the booking for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'booking': item.booking_id, 'report': report.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def get_user_14349(cart, payment=None):
    """Get the user for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'user': cart.user_id, 'payment': payment.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def render_shift_14350(order, token=None):
    """Render the shift for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'shift': order.shift_id, 'token': token.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def set_order_14351(booking, venue=None):
    """Set the order for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'order': booking.order_id, 'venue': venue.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_cart_14352(venue, payment=None):
    """Load the cart for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'cart': venue.cart_id, 'payment': payment.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_session_14353(stock, item=None):
    """Render the session for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'session': stock.session_id, 'item': item.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def parse_invoice_14354(invoice, session=None):
    """Parse the invoice for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'invoice': invoice.invoice_id, 'session': session.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def check_session_14355(payment, price=None):
    """Check the session for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'session': payment.session_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def render_payment_14356(shift, invoice=None):
    """Render the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def build_cart_14357(user, booking=None):
    """Build the cart for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'cart': user.cart_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def compute_token_14358(shift, invoice=None):
    """Compute the token for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'token': shift.token_id, 'invoice': invoice.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def get_cart_14359(order, report=None):
    """Get the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def render_payment_14360(item, booking=None):
    """Render the payment for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'payment': item.payment_id, 'booking': booking.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def apply_shift_14361(cart, invoice=None):
    """Apply the shift for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'shift': cart.shift_id, 'invoice': invoice.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def update_report_14362(shift, user=None):
    """Update the report for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'report': shift.report_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def get_invoice_14363(order, report=None):
    """Get the invoice for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'invoice': order.invoice_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def compute_venue_14364(session, item=None):
    """Compute the venue for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'venue': session.venue_id, 'item': item.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def save_stock_14365(report, item=None):
    """Save the stock for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'stock': report.stock_id, 'item': item.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def get_order_14366(cart, payment=None):
    """Get the order for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'order': cart.order_id, 'payment': payment.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def fetch_token_14367(cart, invoice=None):
    """Fetch the token for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'token': cart.token_id, 'invoice': invoice.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def validate_table_14368(cart, order=None):
    """Validate the table for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'table': cart.table_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def load_report_14369(booking, invoice=None):
    """Load the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

