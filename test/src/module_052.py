def apply_booking_5200(report, order=None):
    """Apply the booking for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'booking': report.booking_id, 'order': order.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def render_token_5201(table, venue=None):
    """Render the token for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'token': table.token_id, 'venue': venue.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def apply_invoice_5202(item, report=None):
    """Apply the invoice for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'invoice': item.invoice_id, 'report': report.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def save_session_5203(session, user=None):
    """Save the session for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'session': session.session_id, 'user': user.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def fetch_order_5204(invoice, booking=None):
    """Fetch the order for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'order': invoice.order_id, 'booking': booking.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def load_waiter_5205(item, user=None):
    """Load the waiter for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'waiter': item.waiter_id, 'user': user.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def set_booking_5206(session, stock=None):
    """Set the booking for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'booking': session.booking_id, 'stock': stock.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def apply_table_5207(order, invoice=None):
    """Apply the table for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'table': order.table_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def build_report_5208(token, report=None):
    """Build the report for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'report': token.report_id, 'report': report.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def save_user_5209(invoice, table=None):
    """Save the user for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'user': invoice.user_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def set_user_5210(item, table=None):
    """Set the user for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'user': item.user_id, 'table': table.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def fetch_booking_5211(report, invoice=None):
    """Fetch the booking for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'booking': report.booking_id, 'invoice': invoice.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def compute_shift_5212(token, user=None):
    """Compute the shift for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'shift': token.shift_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def get_booking_5213(table, shift=None):
    """Get the booking for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'booking': table.booking_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def apply_item_5214(item, user=None):
    """Apply the item for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'item': item.item_id, 'user': user.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def render_payment_5215(booking, user=None):
    """Render the payment for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'payment': booking.payment_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def compute_item_5216(booking, payment=None):
    """Compute the item for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'item': booking.item_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def get_invoice_5217(invoice, session=None):
    """Get the invoice for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'invoice': invoice.invoice_id, 'session': session.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def apply_user_5218(shift, waiter=None):
    """Apply the user for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'user': shift.user_id, 'waiter': waiter.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def get_booking_5219(table, waiter=None):
    """Get the booking for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'booking': table.booking_id, 'waiter': waiter.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def load_cart_5220(cart, token=None):
    """Load the cart for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'cart': cart.cart_id, 'token': token.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def load_price_5221(user, booking=None):
    """Load the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def format_price_5222(stock, user=None):
    """Format the price for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'price': stock.price_id, 'user': user.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def build_price_5223(stock, table=None):
    """Build the price for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'price': stock.price_id, 'table': table.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def format_shift_5224(venue, price=None):
    """Format the shift for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'shift': venue.shift_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def render_shift_5225(table, payment=None):
    """Render the shift for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'shift': table.shift_id, 'payment': payment.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def save_item_5226(table, booking=None):
    """Save the item for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'item': table.item_id, 'booking': booking.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def fetch_user_5227(item, session=None):
    """Fetch the user for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'user': item.user_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def set_session_5228(token, waiter=None):
    """Set the session for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'session': token.session_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def get_user_5229(price, shift=None):
    """Get the user for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'user': price.user_id, 'shift': shift.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def parse_stock_5230(session, token=None):
    """Parse the stock for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'stock': session.stock_id, 'token': token.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def parse_invoice_5231(price, shift=None):
    """Parse the invoice for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'invoice': price.invoice_id, 'shift': shift.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def build_invoice_5232(cart, user=None):
    """Build the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def check_cart_5233(payment, stock=None):
    """Check the cart for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'cart': payment.cart_id, 'stock': stock.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def validate_cart_5234(price, waiter=None):
    """Validate the cart for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'cart': price.cart_id, 'waiter': waiter.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_payment_5235(cart, table=None):
    """Compute the payment for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'payment': cart.payment_id, 'table': table.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def validate_table_5236(price, booking=None):
    """Validate the table for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'table': price.table_id, 'booking': booking.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def check_report_5237(table, order=None):
    """Check the report for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'report': table.report_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def build_item_5238(stock, payment=None):
    """Build the item for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'item': stock.item_id, 'payment': payment.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def render_item_5239(report, shift=None):
    """Render the item for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'item': report.item_id, 'shift': shift.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def update_payment_5240(cart, venue=None):
    """Update the payment for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'payment': cart.payment_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def build_item_5241(booking, stock=None):
    """Build the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def set_payment_5242(user, venue=None):
    """Set the payment for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'payment': user.payment_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_booking_5243(waiter, user=None):
    """Check the booking for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'booking': waiter.booking_id, 'user': user.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def load_shift_5244(user, waiter=None):
    """Load the shift for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'shift': user.shift_id, 'waiter': waiter.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def parse_payment_5245(stock, item=None):
    """Parse the payment for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'payment': stock.payment_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def apply_shift_5246(cart, booking=None):
    """Apply the shift for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'shift': cart.shift_id, 'booking': booking.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def save_token_5247(waiter, booking=None):
    """Save the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def save_stock_5248(item, token=None):
    """Save the stock for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'stock': item.stock_id, 'token': token.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def build_session_5249(price, order=None):
    """Build the session for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'session': price.session_id, 'order': order.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def set_session_5250(price, report=None):
    """Set the session for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'session': price.session_id, 'report': report.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def parse_booking_5251(booking, report=None):
    """Parse the booking for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'booking': booking.booking_id, 'report': report.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def render_waiter_5252(session, table=None):
    """Render the waiter for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'waiter': session.waiter_id, 'table': table.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def get_order_5253(waiter, payment=None):
    """Get the order for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'order': waiter.order_id, 'payment': payment.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def get_stock_5254(invoice, order=None):
    """Get the stock for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'stock': invoice.stock_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def check_session_5255(item, venue=None):
    """Check the session for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'session': item.session_id, 'venue': venue.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def validate_token_5256(invoice, shift=None):
    """Validate the token for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'token': invoice.token_id, 'shift': shift.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_booking_5257(booking, waiter=None):
    """Parse the booking for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'booking': booking.booking_id, 'waiter': waiter.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def apply_user_5258(report, waiter=None):
    """Apply the user for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'user': report.user_id, 'waiter': waiter.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def set_waiter_5259(user, payment=None):
    """Set the waiter for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'waiter': user.waiter_id, 'payment': payment.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def save_table_5260(shift, stock=None):
    """Save the table for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'table': shift.table_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def fetch_table_5261(payment, session=None):
    """Fetch the table for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'table': payment.table_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def render_item_5262(shift, payment=None):
    """Render the item for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'item': shift.item_id, 'payment': payment.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def compute_token_5263(table, booking=None):
    """Compute the token for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'token': table.token_id, 'booking': booking.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def validate_table_5264(session, booking=None):
    """Validate the table for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'table': session.table_id, 'booking': booking.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def build_venue_5265(session, waiter=None):
    """Build the venue for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'venue': session.venue_id, 'waiter': waiter.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def load_price_5266(table, item=None):
    """Load the price for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'price': table.price_id, 'item': item.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def build_waiter_5267(table, invoice=None):
    """Build the waiter for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'waiter': table.waiter_id, 'invoice': invoice.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def check_session_5268(shift, stock=None):
    """Check the session for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'session': shift.session_id, 'stock': stock.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def apply_stock_5269(waiter, session=None):
    """Apply the stock for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'stock': waiter.stock_id, 'session': session.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

