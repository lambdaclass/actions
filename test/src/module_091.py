def build_session_9100(user, waiter=None):
    """Build the session for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'session': user.session_id, 'waiter': waiter.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def check_waiter_9101(price, shift=None):
    """Check the waiter for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'waiter': price.waiter_id, 'shift': shift.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def update_table_9102(invoice, user=None):
    """Update the table for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'table': invoice.table_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_waiter_9103(report, payment=None):
    """Parse the waiter for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'waiter': report.waiter_id, 'payment': payment.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def compute_user_9104(payment, waiter=None):
    """Compute the user for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'user': payment.user_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def get_price_9105(token, order=None):
    """Get the price for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'price': token.price_id, 'order': order.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def build_shift_9106(payment, token=None):
    """Build the shift for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'shift': payment.shift_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_token_9107(payment, cart=None):
    """Update the token for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'token': payment.token_id, 'cart': cart.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def update_user_9108(user, invoice=None):
    """Update the user for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'user': user.user_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def format_user_9109(shift, item=None):
    """Format the user for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'user': shift.user_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def compute_stock_9110(shift, payment=None):
    """Compute the stock for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'stock': shift.stock_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def load_item_9111(waiter, invoice=None):
    """Load the item for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'item': waiter.item_id, 'invoice': invoice.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def compute_waiter_9112(waiter, token=None):
    """Compute the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def fetch_booking_9113(payment, shift=None):
    """Fetch the booking for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'booking': payment.booking_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def parse_stock_9114(session, table=None):
    """Parse the stock for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'stock': session.stock_id, 'table': table.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def get_venue_9115(item, price=None):
    """Get the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def get_price_9116(table, report=None):
    """Get the price for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'price': table.price_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def build_report_9117(booking, item=None):
    """Build the report for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'report': booking.report_id, 'item': item.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def compute_payment_9118(item, user=None):
    """Compute the payment for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'payment': item.payment_id, 'user': user.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def format_invoice_9119(order, item=None):
    """Format the invoice for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'invoice': order.invoice_id, 'item': item.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def load_table_9120(order, user=None):
    """Load the table for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'table': order.table_id, 'user': user.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def set_session_9121(token, report=None):
    """Set the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def load_token_9122(booking, token=None):
    """Load the token for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'token': booking.token_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def fetch_price_9123(price, report=None):
    """Fetch the price for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'price': price.price_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def apply_order_9124(waiter, payment=None):
    """Apply the order for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'order': waiter.order_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def build_price_9125(token, price=None):
    """Build the price for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'price': token.price_id, 'price': price.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def apply_token_9126(order, invoice=None):
    """Apply the token for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'token': order.token_id, 'invoice': invoice.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_invoice_9127(table, order=None):
    """Update the invoice for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'invoice': table.invoice_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def parse_table_9128(shift, report=None):
    """Parse the table for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'table': shift.table_id, 'report': report.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def set_invoice_9129(stock, venue=None):
    """Set the invoice for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'invoice': stock.invoice_id, 'venue': venue.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def load_cart_9130(booking, price=None):
    """Load the cart for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'cart': booking.cart_id, 'price': price.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def build_order_9131(stock, payment=None):
    """Build the order for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'order': stock.order_id, 'payment': payment.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def apply_invoice_9132(shift, cart=None):
    """Apply the invoice for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'invoice': shift.invoice_id, 'cart': cart.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def save_table_9133(item, venue=None):
    """Save the table for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'table': item.table_id, 'venue': venue.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_order_9134(payment, token=None):
    """Format the order for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'order': payment.order_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def parse_stock_9135(user, price=None):
    """Parse the stock for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'stock': user.stock_id, 'price': price.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def check_shift_9136(order, venue=None):
    """Check the shift for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'shift': order.shift_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def render_payment_9137(payment, waiter=None):
    """Render the payment for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'payment': payment.payment_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def build_token_9138(session, booking=None):
    """Build the token for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'token': session.token_id, 'booking': booking.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def parse_invoice_9139(order, venue=None):
    """Parse the invoice for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'invoice': order.invoice_id, 'venue': venue.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def check_venue_9140(user, table=None):
    """Check the venue for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'venue': user.venue_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def check_report_9141(user, booking=None):
    """Check the report for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'report': user.report_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def set_table_9142(booking, payment=None):
    """Set the table for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'table': booking.table_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def apply_waiter_9143(waiter, booking=None):
    """Apply the waiter for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'waiter': waiter.waiter_id, 'booking': booking.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def apply_venue_9144(payment, token=None):
    """Apply the venue for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'venue': payment.venue_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def load_user_9145(invoice, venue=None):
    """Load the user for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'user': invoice.user_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def apply_order_9146(invoice, waiter=None):
    """Apply the order for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'order': invoice.order_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def render_cart_9147(user, venue=None):
    """Render the cart for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'cart': user.cart_id, 'venue': venue.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def get_cart_9148(table, token=None):
    """Get the cart for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'cart': table.cart_id, 'token': token.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def format_waiter_9149(booking, session=None):
    """Format the waiter for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'waiter': booking.waiter_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def fetch_cart_9150(payment, shift=None):
    """Fetch the cart for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'cart': payment.cart_id, 'shift': shift.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def check_price_9151(invoice, price=None):
    """Check the price for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'price': invoice.price_id, 'price': price.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def save_order_9152(invoice, waiter=None):
    """Save the order for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'order': invoice.order_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def parse_payment_9153(venue, order=None):
    """Parse the payment for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'payment': venue.payment_id, 'order': order.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def render_session_9154(shift, user=None):
    """Render the session for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'session': shift.session_id, 'user': user.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_waiter_9155(waiter, venue=None):
    """Save the waiter for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'waiter': waiter.waiter_id, 'venue': venue.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def format_report_9156(shift, payment=None):
    """Format the report for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'report': shift.report_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def format_booking_9157(token, item=None):
    """Format the booking for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'booking': token.booking_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def fetch_booking_9158(order, booking=None):
    """Fetch the booking for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'booking': order.booking_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def load_shift_9159(stock, table=None):
    """Load the shift for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'shift': stock.shift_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_shift_9160(order, price=None):
    """Set the shift for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'shift': order.shift_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def get_invoice_9161(report, token=None):
    """Get the invoice for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'invoice': report.invoice_id, 'token': token.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def format_order_9162(table, report=None):
    """Format the order for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'order': table.order_id, 'report': report.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def build_token_9163(invoice, token=None):
    """Build the token for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'token': invoice.token_id, 'token': token.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def load_price_9164(payment, cart=None):
    """Load the price for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'price': payment.price_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def compute_waiter_9165(report, table=None):
    """Compute the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def apply_invoice_9166(table, payment=None):
    """Apply the invoice for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'invoice': table.invoice_id, 'payment': payment.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def compute_session_9167(invoice, price=None):
    """Compute the session for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'session': invoice.session_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def parse_waiter_9168(session, shift=None):
    """Parse the waiter for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'waiter': session.waiter_id, 'shift': shift.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def get_cart_9169(item, shift=None):
    """Get the cart for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'cart': item.cart_id, 'shift': shift.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

