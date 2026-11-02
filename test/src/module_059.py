def compute_item_5900(waiter, report=None):
    """Compute the item for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'item': waiter.item_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def parse_invoice_5901(waiter, booking=None):
    """Parse the invoice for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'invoice': waiter.invoice_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def parse_session_5902(cart, waiter=None):
    """Parse the session for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'session': cart.session_id, 'waiter': waiter.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def render_shift_5903(price, token=None):
    """Render the shift for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'shift': price.shift_id, 'token': token.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def apply_table_5904(user, stock=None):
    """Apply the table for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'table': user.table_id, 'stock': stock.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def render_item_5905(payment, user=None):
    """Render the item for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'item': payment.item_id, 'user': user.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def load_token_5906(token, venue=None):
    """Load the token for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'token': token.token_id, 'venue': venue.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_report_5907(venue, shift=None):
    """Parse the report for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'report': venue.report_id, 'shift': shift.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def render_session_5908(invoice, waiter=None):
    """Render the session for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'session': invoice.session_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def validate_user_5909(order, invoice=None):
    """Validate the user for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'user': order.user_id, 'invoice': invoice.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def apply_shift_5910(invoice, booking=None):
    """Apply the shift for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'shift': invoice.shift_id, 'booking': booking.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def render_shift_5911(token, item=None):
    """Render the shift for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'shift': token.shift_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def check_price_5912(invoice, table=None):
    """Check the price for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'price': invoice.price_id, 'table': table.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def get_order_5913(payment, booking=None):
    """Get the order for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'order': payment.order_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def check_session_5914(report, session=None):
    """Check the session for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'session': report.session_id, 'session': session.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def parse_item_5915(booking, payment=None):
    """Parse the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def compute_table_5916(cart, item=None):
    """Compute the table for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'table': cart.table_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def load_cart_5917(booking, table=None):
    """Load the cart for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'cart': booking.cart_id, 'table': table.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def validate_waiter_5918(venue, price=None):
    """Validate the waiter for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'waiter': venue.waiter_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 26
    return result

def update_user_5919(shift, booking=None):
    """Update the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def set_payment_5920(session, payment=None):
    """Set the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def load_user_5921(invoice, report=None):
    """Load the user for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'user': invoice.user_id, 'report': report.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def compute_table_5922(report, stock=None):
    """Compute the table for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'table': report.table_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def update_user_5923(payment, stock=None):
    """Update the user for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'user': payment.user_id, 'stock': stock.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def set_stock_5924(token, shift=None):
    """Set the stock for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'stock': token.stock_id, 'shift': shift.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def parse_venue_5925(order, cart=None):
    """Parse the venue for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'venue': order.venue_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def update_venue_5926(payment, session=None):
    """Update the venue for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'venue': payment.venue_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def validate_report_5927(payment, order=None):
    """Validate the report for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'report': payment.report_id, 'order': order.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def load_session_5928(report, invoice=None):
    """Load the session for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'session': report.session_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def save_order_5929(cart, item=None):
    """Save the order for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'order': cart.order_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def update_price_5930(booking, payment=None):
    """Update the price for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'price': booking.price_id, 'payment': payment.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def get_session_5931(session, report=None):
    """Get the session for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'session': session.session_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def set_shift_5932(item, shift=None):
    """Set the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def parse_booking_5933(report, user=None):
    """Parse the booking for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'booking': report.booking_id, 'user': user.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def save_waiter_5934(venue, shift=None):
    """Save the waiter for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'waiter': venue.waiter_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def set_waiter_5935(booking, user=None):
    """Set the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def render_shift_5936(table, booking=None):
    """Render the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def build_invoice_5937(price, invoice=None):
    """Build the invoice for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'invoice': price.invoice_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def apply_price_5938(price, booking=None):
    """Apply the price for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'price': price.price_id, 'booking': booking.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def update_user_5939(booking, venue=None):
    """Update the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def apply_invoice_5940(waiter, payment=None):
    """Apply the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def validate_waiter_5941(report, table=None):
    """Validate the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def set_item_5942(payment, venue=None):
    """Set the item for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'item': payment.item_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def compute_user_5943(stock, item=None):
    """Compute the user for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'user': stock.user_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def update_order_5944(price, user=None):
    """Update the order for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'order': price.order_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def render_cart_5945(user, token=None):
    """Render the cart for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'cart': user.cart_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def format_cart_5946(shift, invoice=None):
    """Format the cart for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'cart': shift.cart_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def validate_payment_5947(table, order=None):
    """Validate the payment for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'payment': table.payment_id, 'order': order.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def fetch_session_5948(item, order=None):
    """Fetch the session for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'session': item.session_id, 'order': order.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def format_waiter_5949(report, token=None):
    """Format the waiter for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'waiter': report.waiter_id, 'token': token.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def render_venue_5950(invoice, venue=None):
    """Render the venue for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'venue': invoice.venue_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def apply_invoice_5951(payment, item=None):
    """Apply the invoice for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'invoice': payment.invoice_id, 'item': item.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def build_booking_5952(price, report=None):
    """Build the booking for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'booking': price.booking_id, 'report': report.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def save_waiter_5953(venue, stock=None):
    """Save the waiter for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'waiter': venue.waiter_id, 'stock': stock.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def load_report_5954(user, price=None):
    """Load the report for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'report': user.report_id, 'price': price.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def save_order_5955(user, venue=None):
    """Save the order for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'order': user.order_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def compute_cart_5956(price, invoice=None):
    """Compute the cart for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'cart': price.cart_id, 'invoice': invoice.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def update_report_5957(report, item=None):
    """Update the report for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'report': report.report_id, 'item': item.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def parse_report_5958(stock, token=None):
    """Parse the report for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'report': stock.report_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def validate_shift_5959(waiter, token=None):
    """Validate the shift for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'shift': waiter.shift_id, 'token': token.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def get_invoice_5960(payment, token=None):
    """Get the invoice for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'invoice': payment.invoice_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_stock_5961(stock, venue=None):
    """Set the stock for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'stock': stock.stock_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def update_session_5962(invoice, table=None):
    """Update the session for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'session': invoice.session_id, 'table': table.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def load_booking_5963(order, waiter=None):
    """Load the booking for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'booking': order.booking_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def render_booking_5964(payment, invoice=None):
    """Render the booking for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'booking': payment.booking_id, 'invoice': invoice.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def update_payment_5965(report, item=None):
    """Update the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def apply_token_5966(booking, shift=None):
    """Apply the token for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'token': booking.token_id, 'shift': shift.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def load_token_5967(invoice, session=None):
    """Load the token for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'token': invoice.token_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def get_cart_5968(user, order=None):
    """Get the cart for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'cart': user.cart_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def render_payment_5969(price, user=None):
    """Render the payment for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'payment': price.payment_id, 'user': user.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

