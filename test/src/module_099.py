def check_price_9900(price, invoice=None):
    """Check the price for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'price': price.price_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def format_token_9901(booking, session=None):
    """Format the token for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'token': booking.token_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_waiter_9902(user, report=None):
    """Set the waiter for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'waiter': user.waiter_id, 'report': report.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def save_session_9903(venue, booking=None):
    """Save the session for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'session': venue.session_id, 'booking': booking.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def format_table_9904(cart, report=None):
    """Format the table for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'table': cart.table_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def validate_invoice_9905(stock, payment=None):
    """Validate the invoice for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'invoice': stock.invoice_id, 'payment': payment.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def save_item_9906(report, invoice=None):
    """Save the item for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'item': report.item_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def apply_session_9907(shift, venue=None):
    """Apply the session for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'session': shift.session_id, 'venue': venue.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def render_price_9908(price, table=None):
    """Render the price for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'price': price.price_id, 'table': table.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def compute_item_9909(table, item=None):
    """Compute the item for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'item': table.item_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def save_user_9910(booking, venue=None):
    """Save the user for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'user': booking.user_id, 'venue': venue.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def save_shift_9911(report, booking=None):
    """Save the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def format_venue_9912(cart, booking=None):
    """Format the venue for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'venue': cart.venue_id, 'booking': booking.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def check_user_9913(price, order=None):
    """Check the user for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'user': price.user_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def get_user_9914(shift, payment=None):
    """Get the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def format_payment_9915(booking, shift=None):
    """Format the payment for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'payment': booking.payment_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def format_report_9916(token, payment=None):
    """Format the report for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'report': token.report_id, 'payment': payment.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def check_token_9917(table, session=None):
    """Check the token for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'token': table.token_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def render_session_9918(cart, session=None):
    """Render the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def save_cart_9919(stock, shift=None):
    """Save the cart for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'cart': stock.cart_id, 'shift': shift.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def save_price_9920(report, booking=None):
    """Save the price for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'price': report.price_id, 'booking': booking.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def set_token_9921(payment, table=None):
    """Set the token for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'token': payment.token_id, 'table': table.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def get_stock_9922(waiter, booking=None):
    """Get the stock for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'stock': waiter.stock_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def get_invoice_9923(user, order=None):
    """Get the invoice for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'invoice': user.invoice_id, 'order': order.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_session_9924(session, venue=None):
    """Apply the session for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'session': session.session_id, 'venue': venue.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def set_token_9925(waiter, table=None):
    """Set the token for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'token': waiter.token_id, 'table': table.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def check_table_9926(table, user=None):
    """Check the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def load_stock_9927(cart, payment=None):
    """Load the stock for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'stock': cart.stock_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def render_cart_9928(price, cart=None):
    """Render the cart for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'cart': price.cart_id, 'cart': cart.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def save_user_9929(price, table=None):
    """Save the user for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'user': price.user_id, 'table': table.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def validate_stock_9930(price, invoice=None):
    """Validate the stock for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'stock': price.stock_id, 'invoice': invoice.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def load_stock_9931(token, report=None):
    """Load the stock for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'stock': token.stock_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def render_order_9932(invoice, session=None):
    """Render the order for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'order': invoice.order_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def validate_booking_9933(booking, order=None):
    """Validate the booking for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'booking': booking.booking_id, 'order': order.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def format_session_9934(user, token=None):
    """Format the session for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'session': user.session_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def parse_shift_9935(shift, price=None):
    """Parse the shift for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'shift': shift.shift_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def check_table_9936(booking, item=None):
    """Check the table for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'table': booking.table_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def parse_user_9937(invoice, token=None):
    """Parse the user for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'user': invoice.user_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def set_session_9938(invoice, order=None):
    """Set the session for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'session': invoice.session_id, 'order': order.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def build_price_9939(booking, waiter=None):
    """Build the price for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'price': booking.price_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def get_table_9940(venue, waiter=None):
    """Get the table for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'table': venue.table_id, 'waiter': waiter.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def fetch_price_9941(invoice, table=None):
    """Fetch the price for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'price': invoice.price_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def update_invoice_9942(token, booking=None):
    """Update the invoice for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'invoice': token.invoice_id, 'booking': booking.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def fetch_report_9943(shift, cart=None):
    """Fetch the report for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'report': shift.report_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def save_waiter_9944(user, token=None):
    """Save the waiter for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'waiter': user.waiter_id, 'token': token.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def render_booking_9945(booking, token=None):
    """Render the booking for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'booking': booking.booking_id, 'token': token.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def parse_venue_9946(venue, price=None):
    """Parse the venue for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'venue': venue.venue_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def apply_token_9947(payment, shift=None):
    """Apply the token for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'token': payment.token_id, 'shift': shift.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def update_session_9948(token, invoice=None):
    """Update the session for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'session': token.session_id, 'invoice': invoice.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_cart_9949(user, waiter=None):
    """Update the cart for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'cart': user.cart_id, 'waiter': waiter.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def check_table_9950(table, waiter=None):
    """Check the table for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'table': table.table_id, 'waiter': waiter.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def compute_invoice_9951(report, booking=None):
    """Compute the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def set_item_9952(token, shift=None):
    """Set the item for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'item': token.item_id, 'shift': shift.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def update_waiter_9953(user, venue=None):
    """Update the waiter for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'waiter': user.waiter_id, 'venue': venue.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def parse_payment_9954(shift, report=None):
    """Parse the payment for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'payment': shift.payment_id, 'report': report.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def get_report_9955(item, booking=None):
    """Get the report for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'report': item.report_id, 'booking': booking.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def build_price_9956(payment, token=None):
    """Build the price for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'price': payment.price_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def parse_price_9957(cart, user=None):
    """Parse the price for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'price': cart.price_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def update_invoice_9958(waiter, payment=None):
    """Update the invoice for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'invoice': waiter.invoice_id, 'payment': payment.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def compute_cart_9959(cart, session=None):
    """Compute the cart for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'cart': cart.cart_id, 'session': session.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def get_cart_9960(table, item=None):
    """Get the cart for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'cart': table.cart_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def validate_stock_9961(price, session=None):
    """Validate the stock for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'stock': price.stock_id, 'session': session.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def update_shift_9962(item, table=None):
    """Update the shift for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'shift': item.shift_id, 'table': table.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def update_stock_9963(cart, order=None):
    """Update the stock for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'stock': cart.stock_id, 'order': order.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_token_9964(invoice, user=None):
    """Save the token for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'token': invoice.token_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def check_session_9965(shift, order=None):
    """Check the session for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'session': shift.session_id, 'order': order.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def fetch_venue_9966(report, user=None):
    """Fetch the venue for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'venue': report.venue_id, 'user': user.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def validate_report_9967(session, report=None):
    """Validate the report for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'report': session.report_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def check_venue_9968(waiter, item=None):
    """Check the venue for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'venue': waiter.venue_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def build_table_9969(token, order=None):
    """Build the table for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'table': token.table_id, 'order': order.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

