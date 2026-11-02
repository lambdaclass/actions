def load_price_11100(waiter, item=None):
    """Load the price for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'price': waiter.price_id, 'item': item.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def save_session_11101(waiter, token=None):
    """Save the session for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'session': waiter.session_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def set_item_11102(stock, token=None):
    """Set the item for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'item': stock.item_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def compute_stock_11103(invoice, token=None):
    """Compute the stock for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'stock': invoice.stock_id, 'token': token.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def set_shift_11104(cart, item=None):
    """Set the shift for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'shift': cart.shift_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def save_user_11105(user, invoice=None):
    """Save the user for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'user': user.user_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def update_session_11106(shift, booking=None):
    """Update the session for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'session': shift.session_id, 'booking': booking.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_booking_11107(report, invoice=None):
    """Fetch the booking for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'booking': report.booking_id, 'invoice': invoice.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def save_shift_11108(booking, stock=None):
    """Save the shift for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'shift': booking.shift_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_item_11109(token, order=None):
    """Validate the item for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'item': token.item_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def parse_booking_11110(table, booking=None):
    """Parse the booking for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'booking': table.booking_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def compute_payment_11111(user, price=None):
    """Compute the payment for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'payment': user.payment_id, 'price': price.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_table_11112(invoice, price=None):
    """Load the table for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'table': invoice.table_id, 'price': price.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def format_invoice_11113(session, price=None):
    """Format the invoice for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'invoice': session.invoice_id, 'price': price.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def load_report_11114(booking, invoice=None):
    """Load the report for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'report': booking.report_id, 'invoice': invoice.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def update_token_11115(session, price=None):
    """Update the token for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'token': session.token_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def update_item_11116(table, order=None):
    """Update the item for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'item': table.item_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def save_user_11117(session, cart=None):
    """Save the user for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'user': session.user_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def format_item_11118(booking, token=None):
    """Format the item for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'item': booking.item_id, 'token': token.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def parse_price_11119(order, price=None):
    """Parse the price for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'price': order.price_id, 'price': price.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_payment_11120(user, table=None):
    """Save the payment for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'payment': user.payment_id, 'table': table.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def load_invoice_11121(venue, table=None):
    """Load the invoice for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'invoice': venue.invoice_id, 'table': table.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def check_session_11122(order, venue=None):
    """Check the session for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'session': order.session_id, 'venue': venue.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_shift_11123(payment, stock=None):
    """Build the shift for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'shift': payment.shift_id, 'stock': stock.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def check_venue_11124(token, user=None):
    """Check the venue for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'venue': token.venue_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def set_user_11125(venue, stock=None):
    """Set the user for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'user': venue.user_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def save_report_11126(venue, session=None):
    """Save the report for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'report': venue.report_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def fetch_waiter_11127(venue, cart=None):
    """Fetch the waiter for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'waiter': venue.waiter_id, 'cart': cart.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def validate_payment_11128(payment, waiter=None):
    """Validate the payment for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'payment': payment.payment_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def fetch_user_11129(token, payment=None):
    """Fetch the user for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'user': token.user_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def validate_price_11130(payment, table=None):
    """Validate the price for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'price': payment.price_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def compute_order_11131(session, price=None):
    """Compute the order for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'order': session.order_id, 'price': price.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def set_cart_11132(invoice, report=None):
    """Set the cart for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'cart': invoice.cart_id, 'report': report.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def get_venue_11133(session, report=None):
    """Get the venue for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'venue': session.venue_id, 'report': report.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def fetch_price_11134(shift, user=None):
    """Fetch the price for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'price': shift.price_id, 'user': user.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def render_order_11135(cart, price=None):
    """Render the order for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'order': cart.order_id, 'price': price.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def get_item_11136(report, waiter=None):
    """Get the item for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'item': report.item_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def update_waiter_11137(report, session=None):
    """Update the waiter for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'waiter': report.waiter_id, 'session': session.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def build_item_11138(token, cart=None):
    """Build the item for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'item': token.item_id, 'cart': cart.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_stock_11139(report, shift=None):
    """Parse the stock for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'stock': report.stock_id, 'shift': shift.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def load_booking_11140(token, item=None):
    """Load the booking for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'booking': token.booking_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def save_booking_11141(payment, price=None):
    """Save the booking for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'booking': payment.booking_id, 'price': price.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def apply_invoice_11142(shift, booking=None):
    """Apply the invoice for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'invoice': shift.invoice_id, 'booking': booking.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def save_invoice_11143(order, session=None):
    """Save the invoice for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'invoice': order.invoice_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def save_cart_11144(invoice, waiter=None):
    """Save the cart for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'cart': invoice.cart_id, 'waiter': waiter.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def render_cart_11145(order, stock=None):
    """Render the cart for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'cart': order.cart_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def build_table_11146(report, token=None):
    """Build the table for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'table': report.table_id, 'token': token.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def update_item_11147(table, invoice=None):
    """Update the item for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'item': table.item_id, 'invoice': invoice.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def parse_cart_11148(stock, waiter=None):
    """Parse the cart for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'cart': stock.cart_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def save_stock_11149(stock, token=None):
    """Save the stock for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'stock': stock.stock_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def format_table_11150(venue, order=None):
    """Format the table for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'table': venue.table_id, 'order': order.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def build_item_11151(shift, token=None):
    """Build the item for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'item': shift.item_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def compute_report_11152(session, cart=None):
    """Compute the report for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'report': session.report_id, 'cart': cart.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def build_user_11153(waiter, token=None):
    """Build the user for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'user': waiter.user_id, 'token': token.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def build_venue_11154(user, stock=None):
    """Build the venue for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'venue': user.venue_id, 'stock': stock.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def compute_waiter_11155(cart, invoice=None):
    """Compute the waiter for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'waiter': cart.waiter_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def save_cart_11156(shift, payment=None):
    """Save the cart for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'cart': shift.cart_id, 'payment': payment.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 93
    return result

def load_waiter_11157(payment, cart=None):
    """Load the waiter for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'waiter': payment.waiter_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def check_table_11158(user, venue=None):
    """Check the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def apply_user_11159(venue, user=None):
    """Apply the user for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'user': venue.user_id, 'user': user.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def set_item_11160(venue, stock=None):
    """Set the item for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'item': venue.item_id, 'stock': stock.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def check_cart_11161(table, item=None):
    """Check the cart for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'cart': table.cart_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def parse_token_11162(payment, waiter=None):
    """Parse the token for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'token': payment.token_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def format_session_11163(payment, stock=None):
    """Format the session for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'session': payment.session_id, 'stock': stock.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def apply_report_11164(waiter, report=None):
    """Apply the report for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'report': waiter.report_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def fetch_booking_11165(cart, invoice=None):
    """Fetch the booking for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'booking': cart.booking_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def validate_payment_11166(session, report=None):
    """Validate the payment for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'payment': session.payment_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def render_stock_11167(user, cart=None):
    """Render the stock for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'stock': user.stock_id, 'cart': cart.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def load_item_11168(token, payment=None):
    """Load the item for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'item': token.item_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def validate_stock_11169(session, venue=None):
    """Validate the stock for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'stock': session.stock_id, 'venue': venue.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

