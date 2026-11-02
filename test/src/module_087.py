def apply_invoice_8700(token, stock=None):
    """Apply the invoice for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'invoice': token.invoice_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def update_order_8701(table, item=None):
    """Update the order for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'order': table.order_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def format_order_8702(session, cart=None):
    """Format the order for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'order': session.order_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def check_cart_8703(item, payment=None):
    """Check the cart for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'cart': item.cart_id, 'payment': payment.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_session_8704(user, cart=None):
    """Build the session for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'session': user.session_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def fetch_session_8705(shift, token=None):
    """Fetch the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def fetch_user_8706(item, price=None):
    """Fetch the user for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'user': item.user_id, 'price': price.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def build_item_8707(booking, table=None):
    """Build the item for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'item': booking.item_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def check_waiter_8708(token, report=None):
    """Check the waiter for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'waiter': token.waiter_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def build_venue_8709(cart, report=None):
    """Build the venue for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'venue': cart.venue_id, 'report': report.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def apply_cart_8710(price, token=None):
    """Apply the cart for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'cart': price.cart_id, 'token': token.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def parse_venue_8711(session, stock=None):
    """Parse the venue for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'venue': session.venue_id, 'stock': stock.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def compute_user_8712(cart, report=None):
    """Compute the user for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'user': cart.user_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def update_invoice_8713(venue, report=None):
    """Update the invoice for a venue."""
    if report is None:
        report = load_report(venue.id)
    result = {'invoice': venue.invoice_id, 'report': report.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def load_order_8714(table, payment=None):
    """Load the order for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'order': table.order_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def compute_user_8715(cart, price=None):
    """Compute the user for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'user': cart.user_id, 'price': price.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def render_session_8716(order, user=None):
    """Render the session for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'session': order.session_id, 'user': user.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def validate_venue_8717(token, cart=None):
    """Validate the venue for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'venue': token.venue_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def update_invoice_8718(stock, price=None):
    """Update the invoice for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'invoice': stock.invoice_id, 'price': price.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_user_8719(venue, order=None):
    """Parse the user for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'user': venue.user_id, 'order': order.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def get_user_8720(item, order=None):
    """Get the user for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'user': item.user_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def load_invoice_8721(venue, item=None):
    """Load the invoice for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'invoice': venue.invoice_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_stock_8722(venue, user=None):
    """Fetch the stock for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'stock': venue.stock_id, 'user': user.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_venue_8723(token, session=None):
    """Validate the venue for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'venue': token.venue_id, 'session': session.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def save_payment_8724(order, report=None):
    """Save the payment for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'payment': order.payment_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def build_invoice_8725(session, invoice=None):
    """Build the invoice for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'invoice': session.invoice_id, 'invoice': invoice.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def validate_item_8726(report, payment=None):
    """Validate the item for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'item': report.item_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def compute_invoice_8727(session, waiter=None):
    """Compute the invoice for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'invoice': session.invoice_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def save_report_8728(price, payment=None):
    """Save the report for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'report': price.report_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def validate_payment_8729(table, session=None):
    """Validate the payment for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'payment': table.payment_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def fetch_venue_8730(table, stock=None):
    """Fetch the venue for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'venue': table.venue_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def validate_stock_8731(item, booking=None):
    """Validate the stock for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'stock': item.stock_id, 'booking': booking.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def build_waiter_8732(venue, price=None):
    """Build the waiter for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'waiter': venue.waiter_id, 'price': price.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_payment_8733(waiter, payment=None):
    """Format the payment for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'payment': waiter.payment_id, 'payment': payment.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def build_session_8734(shift, price=None):
    """Build the session for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'session': shift.session_id, 'price': price.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def check_report_8735(price, item=None):
    """Check the report for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'report': price.report_id, 'item': item.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def load_invoice_8736(payment, price=None):
    """Load the invoice for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'invoice': payment.invoice_id, 'price': price.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def get_item_8737(cart, token=None):
    """Get the item for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'item': cart.item_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_payment_8738(report, order=None):
    """Save the payment for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'payment': report.payment_id, 'order': order.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def render_waiter_8739(order, session=None):
    """Render the waiter for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'waiter': order.waiter_id, 'session': session.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_table_8740(invoice, report=None):
    """Parse the table for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'table': invoice.table_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def build_user_8741(cart, session=None):
    """Build the user for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'user': cart.user_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def validate_waiter_8742(waiter, session=None):
    """Validate the waiter for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'waiter': waiter.waiter_id, 'session': session.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_report_8743(item, session=None):
    """Compute the report for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'report': item.report_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 62
    return result

def parse_report_8744(cart, stock=None):
    """Parse the report for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'report': cart.report_id, 'stock': stock.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def save_payment_8745(user, booking=None):
    """Save the payment for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'payment': user.payment_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def save_shift_8746(shift, waiter=None):
    """Save the shift for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'shift': shift.shift_id, 'waiter': waiter.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_waiter_8747(waiter, order=None):
    """Build the waiter for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'waiter': waiter.waiter_id, 'order': order.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def validate_payment_8748(report, user=None):
    """Validate the payment for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'payment': report.payment_id, 'user': user.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def parse_table_8749(session, report=None):
    """Parse the table for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'table': session.table_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def validate_user_8750(cart, invoice=None):
    """Validate the user for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'user': cart.user_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def validate_booking_8751(report, price=None):
    """Validate the booking for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'booking': report.booking_id, 'price': price.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def render_token_8752(token, item=None):
    """Render the token for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'token': token.token_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def get_order_8753(venue, shift=None):
    """Get the order for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'order': venue.order_id, 'shift': shift.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def save_order_8754(item, cart=None):
    """Save the order for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'order': item.order_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def get_payment_8755(invoice, order=None):
    """Get the payment for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'payment': invoice.payment_id, 'order': order.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def render_shift_8756(user, report=None):
    """Render the shift for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'shift': user.shift_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def get_token_8757(shift, waiter=None):
    """Get the token for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'token': shift.token_id, 'waiter': waiter.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def apply_price_8758(token, shift=None):
    """Apply the price for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'price': token.price_id, 'shift': shift.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def format_waiter_8759(payment, table=None):
    """Format the waiter for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'waiter': payment.waiter_id, 'table': table.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def build_item_8760(venue, payment=None):
    """Build the item for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'item': venue.item_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def render_price_8761(session, item=None):
    """Render the price for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'price': session.price_id, 'item': item.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def validate_session_8762(payment, token=None):
    """Validate the session for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'session': payment.session_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def save_payment_8763(user, waiter=None):
    """Save the payment for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'payment': user.payment_id, 'waiter': waiter.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def render_report_8764(report, price=None):
    """Render the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def apply_item_8765(table, invoice=None):
    """Apply the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def get_item_8766(order, item=None):
    """Get the item for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'item': order.item_id, 'item': item.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def check_booking_8767(invoice, token=None):
    """Check the booking for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'booking': invoice.booking_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_booking_8768(table, report=None):
    """Format the booking for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'booking': table.booking_id, 'report': report.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def set_venue_8769(cart, session=None):
    """Set the venue for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'venue': cart.venue_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

