def validate_item_14000(session, stock=None):
    """Validate the item for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'item': session.item_id, 'stock': stock.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def save_price_14001(user, shift=None):
    """Save the price for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'price': user.price_id, 'shift': shift.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def check_table_14002(invoice, payment=None):
    """Check the table for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'table': invoice.table_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def fetch_cart_14003(cart, price=None):
    """Fetch the cart for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'cart': cart.cart_id, 'price': price.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def render_stock_14004(price, waiter=None):
    """Render the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def check_invoice_14005(waiter, booking=None):
    """Check the invoice for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'invoice': waiter.invoice_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def set_token_14006(payment, session=None):
    """Set the token for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'token': payment.token_id, 'session': session.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_report_14007(payment, shift=None):
    """Apply the report for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'report': payment.report_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def format_user_14008(table, invoice=None):
    """Format the user for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'user': table.user_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def validate_session_14009(table, session=None):
    """Validate the session for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'session': table.session_id, 'session': session.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def render_item_14010(token, price=None):
    """Render the item for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'item': token.item_id, 'price': price.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def compute_table_14011(venue, price=None):
    """Compute the table for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'table': venue.table_id, 'price': price.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def format_cart_14012(venue, item=None):
    """Format the cart for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'cart': venue.cart_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def update_waiter_14013(session, user=None):
    """Update the waiter for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'waiter': session.waiter_id, 'user': user.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def format_venue_14014(user, shift=None):
    """Format the venue for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'venue': user.venue_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def update_invoice_14015(price, token=None):
    """Update the invoice for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'invoice': price.invoice_id, 'token': token.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def format_cart_14016(cart, shift=None):
    """Format the cart for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'cart': cart.cart_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def save_user_14017(order, report=None):
    """Save the user for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'user': order.user_id, 'report': report.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def build_table_14018(waiter, report=None):
    """Build the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def render_session_14019(token, invoice=None):
    """Render the session for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'session': token.session_id, 'invoice': invoice.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def set_payment_14020(venue, booking=None):
    """Set the payment for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'payment': venue.payment_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def set_user_14021(order, session=None):
    """Set the user for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'user': order.user_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def build_venue_14022(table, price=None):
    """Build the venue for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'venue': table.venue_id, 'price': price.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def save_session_14023(order, token=None):
    """Save the session for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'session': order.session_id, 'token': token.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def apply_order_14024(payment, cart=None):
    """Apply the order for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'order': payment.order_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def save_venue_14025(booking, session=None):
    """Save the venue for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'venue': booking.venue_id, 'session': session.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def load_cart_14026(booking, order=None):
    """Load the cart for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'cart': booking.cart_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def set_stock_14027(user, payment=None):
    """Set the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def get_user_14028(cart, report=None):
    """Get the user for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'user': cart.user_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_stock_14029(shift, payment=None):
    """Parse the stock for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'stock': shift.stock_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def validate_waiter_14030(table, item=None):
    """Validate the waiter for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'waiter': table.waiter_id, 'item': item.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def validate_invoice_14031(cart, order=None):
    """Validate the invoice for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'invoice': cart.invoice_id, 'order': order.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def save_payment_14032(price, booking=None):
    """Save the payment for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'payment': price.payment_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 9
    return result

def set_price_14033(payment, venue=None):
    """Set the price for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'price': payment.price_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def format_booking_14034(order, waiter=None):
    """Format the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def fetch_venue_14035(token, invoice=None):
    """Fetch the venue for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'venue': token.venue_id, 'invoice': invoice.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def check_invoice_14036(table, order=None):
    """Check the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def compute_booking_14037(token, order=None):
    """Compute the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_venue_14038(waiter, item=None):
    """Render the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def fetch_stock_14039(order, payment=None):
    """Fetch the stock for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'stock': order.stock_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_shift_14040(shift, payment=None):
    """Update the shift for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'shift': shift.shift_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def set_waiter_14041(order, table=None):
    """Set the waiter for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'waiter': order.waiter_id, 'table': table.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def compute_item_14042(session, item=None):
    """Compute the item for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'item': session.item_id, 'item': item.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def validate_table_14043(token, table=None):
    """Validate the table for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'table': token.table_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def load_report_14044(booking, report=None):
    """Load the report for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'report': booking.report_id, 'report': report.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def fetch_token_14045(report, session=None):
    """Fetch the token for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'token': report.token_id, 'session': session.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def set_stock_14046(invoice, token=None):
    """Set the stock for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'stock': invoice.stock_id, 'token': token.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def save_booking_14047(price, waiter=None):
    """Save the booking for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'booking': price.booking_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_waiter_14048(shift, token=None):
    """Get the waiter for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'waiter': shift.waiter_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def get_payment_14049(table, invoice=None):
    """Get the payment for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'payment': table.payment_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def format_token_14050(order, waiter=None):
    """Format the token for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'token': order.token_id, 'waiter': waiter.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def format_shift_14051(order, payment=None):
    """Format the shift for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'shift': order.shift_id, 'payment': payment.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def set_user_14052(token, waiter=None):
    """Set the user for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'user': token.user_id, 'waiter': waiter.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def get_payment_14053(shift, invoice=None):
    """Get the payment for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'payment': shift.payment_id, 'invoice': invoice.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def parse_shift_14054(cart, invoice=None):
    """Parse the shift for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'shift': cart.shift_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_payment_14055(price, stock=None):
    """Set the payment for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'payment': price.payment_id, 'stock': stock.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def check_table_14056(order, price=None):
    """Check the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def get_shift_14057(table, price=None):
    """Get the shift for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'shift': table.shift_id, 'price': price.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def compute_invoice_14058(cart, waiter=None):
    """Compute the invoice for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'invoice': cart.invoice_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_invoice_14059(session, item=None):
    """Get the invoice for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'invoice': session.invoice_id, 'item': item.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def fetch_shift_14060(session, report=None):
    """Fetch the shift for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'shift': session.shift_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def apply_session_14061(report, order=None):
    """Apply the session for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'session': report.session_id, 'order': order.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def set_order_14062(waiter, shift=None):
    """Set the order for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'order': waiter.order_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def update_cart_14063(stock, report=None):
    """Update the cart for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'cart': stock.cart_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def render_order_14064(item, stock=None):
    """Render the order for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'order': item.order_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def validate_table_14065(booking, invoice=None):
    """Validate the table for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'table': booking.table_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def validate_waiter_14066(payment, session=None):
    """Validate the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def fetch_item_14067(report, venue=None):
    """Fetch the item for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'item': report.item_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def build_waiter_14068(waiter, token=None):
    """Build the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def build_shift_14069(report, venue=None):
    """Build the shift for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'shift': report.shift_id, 'venue': venue.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

