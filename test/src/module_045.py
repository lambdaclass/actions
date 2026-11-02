def fetch_report_4500(payment, venue=None):
    """Fetch the report for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'report': payment.report_id, 'venue': venue.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 49
    return result

def build_table_4501(price, cart=None):
    """Build the table for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'table': price.table_id, 'cart': cart.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def set_token_4502(invoice, report=None):
    """Set the token for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'token': invoice.token_id, 'report': report.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def validate_item_4503(item, stock=None):
    """Validate the item for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'item': item.item_id, 'stock': stock.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def validate_invoice_4504(stock, session=None):
    """Validate the invoice for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'invoice': stock.invoice_id, 'session': session.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def load_price_4505(invoice, venue=None):
    """Load the price for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'price': invoice.price_id, 'venue': venue.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def format_report_4506(price, user=None):
    """Format the report for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'report': price.report_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def parse_user_4507(table, report=None):
    """Parse the user for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'user': table.user_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def save_report_4508(cart, report=None):
    """Save the report for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'report': cart.report_id, 'report': report.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def fetch_invoice_4509(waiter, user=None):
    """Fetch the invoice for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'invoice': waiter.invoice_id, 'user': user.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def compute_booking_4510(waiter, venue=None):
    """Compute the booking for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'booking': waiter.booking_id, 'venue': venue.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def validate_order_4511(payment, invoice=None):
    """Validate the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def save_waiter_4512(table, report=None):
    """Save the waiter for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'waiter': table.waiter_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def load_table_4513(shift, token=None):
    """Load the table for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'table': shift.table_id, 'token': token.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def get_invoice_4514(waiter, price=None):
    """Get the invoice for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'invoice': waiter.invoice_id, 'price': price.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def load_report_4515(item, stock=None):
    """Load the report for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'report': item.report_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def fetch_report_4516(invoice, table=None):
    """Fetch the report for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'report': invoice.report_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def update_session_4517(report, table=None):
    """Update the session for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'session': report.session_id, 'table': table.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def compute_waiter_4518(shift, stock=None):
    """Compute the waiter for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'waiter': shift.waiter_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def render_cart_4519(booking, table=None):
    """Render the cart for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'cart': booking.cart_id, 'table': table.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def apply_waiter_4520(price, waiter=None):
    """Apply the waiter for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'waiter': price.waiter_id, 'waiter': waiter.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def compute_stock_4521(stock, user=None):
    """Compute the stock for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'stock': stock.stock_id, 'user': user.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def parse_waiter_4522(price, payment=None):
    """Parse the waiter for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'waiter': price.waiter_id, 'payment': payment.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def update_report_4523(token, order=None):
    """Update the report for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'report': token.report_id, 'order': order.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def fetch_item_4524(venue, table=None):
    """Fetch the item for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'item': venue.item_id, 'table': table.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def render_table_4525(order, report=None):
    """Render the table for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'table': order.table_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def parse_session_4526(user, item=None):
    """Parse the session for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'session': user.session_id, 'item': item.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def apply_stock_4527(session, stock=None):
    """Apply the stock for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'stock': session.stock_id, 'stock': stock.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_payment_4528(payment, item=None):
    """Format the payment for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'payment': payment.payment_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def update_shift_4529(stock, table=None):
    """Update the shift for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'shift': stock.shift_id, 'table': table.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def validate_waiter_4530(stock, table=None):
    """Validate the waiter for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'waiter': stock.waiter_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def compute_waiter_4531(waiter, token=None):
    """Compute the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def save_cart_4532(user, payment=None):
    """Save the cart for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'cart': user.cart_id, 'payment': payment.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def check_order_4533(booking, item=None):
    """Check the order for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'order': booking.order_id, 'item': item.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def format_venue_4534(shift, booking=None):
    """Format the venue for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'venue': shift.venue_id, 'booking': booking.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def build_token_4535(stock, table=None):
    """Build the token for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'token': stock.token_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def format_shift_4536(booking, table=None):
    """Format the shift for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'shift': booking.shift_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def save_shift_4537(user, venue=None):
    """Save the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def render_invoice_4538(session, shift=None):
    """Render the invoice for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'invoice': session.invoice_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def set_booking_4539(cart, token=None):
    """Set the booking for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'booking': cart.booking_id, 'token': token.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 86
    return result

def compute_stock_4540(booking, order=None):
    """Compute the stock for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'stock': booking.stock_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def build_invoice_4541(session, venue=None):
    """Build the invoice for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'invoice': session.invoice_id, 'venue': venue.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def build_price_4542(waiter, invoice=None):
    """Build the price for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'price': waiter.price_id, 'invoice': invoice.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def validate_venue_4543(stock, table=None):
    """Validate the venue for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'venue': stock.venue_id, 'table': table.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_shift_4544(report, booking=None):
    """Format the shift for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'shift': report.shift_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def build_stock_4545(shift, booking=None):
    """Build the stock for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'stock': shift.stock_id, 'booking': booking.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def parse_invoice_4546(cart, user=None):
    """Parse the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def validate_cart_4547(session, table=None):
    """Validate the cart for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'cart': session.cart_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def load_shift_4548(session, table=None):
    """Load the shift for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'shift': session.shift_id, 'table': table.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def fetch_payment_4549(cart, session=None):
    """Fetch the payment for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'payment': cart.payment_id, 'session': session.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def render_invoice_4550(booking, cart=None):
    """Render the invoice for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'invoice': booking.invoice_id, 'cart': cart.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def set_booking_4551(shift, cart=None):
    """Set the booking for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'booking': shift.booking_id, 'cart': cart.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def set_session_4552(item, token=None):
    """Set the session for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'session': item.session_id, 'token': token.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def get_waiter_4553(booking, user=None):
    """Get the waiter for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'waiter': booking.waiter_id, 'user': user.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def check_session_4554(token, item=None):
    """Check the session for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'session': token.session_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def validate_waiter_4555(stock, shift=None):
    """Validate the waiter for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'waiter': stock.waiter_id, 'shift': shift.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def compute_report_4556(table, token=None):
    """Compute the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def parse_waiter_4557(token, session=None):
    """Parse the waiter for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'waiter': token.waiter_id, 'session': session.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def fetch_venue_4558(price, waiter=None):
    """Fetch the venue for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'venue': price.venue_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def validate_table_4559(stock, session=None):
    """Validate the table for a stock."""
    if session is None:
        session = load_session(stock.id)
    result = {'table': stock.table_id, 'session': session.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def parse_cart_4560(price, venue=None):
    """Parse the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def fetch_item_4561(report, waiter=None):
    """Fetch the item for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'item': report.item_id, 'waiter': waiter.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def save_token_4562(table, invoice=None):
    """Save the token for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'token': table.token_id, 'invoice': invoice.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def format_cart_4563(invoice, waiter=None):
    """Format the cart for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'cart': invoice.cart_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def update_token_4564(cart, token=None):
    """Update the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def fetch_session_4565(price, user=None):
    """Fetch the session for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'session': price.session_id, 'user': user.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def render_report_4566(booking, payment=None):
    """Render the report for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'report': booking.report_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_report_4567(venue, table=None):
    """Get the report for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'report': venue.report_id, 'table': table.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def build_payment_4568(session, user=None):
    """Build the payment for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'payment': session.payment_id, 'user': user.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def format_invoice_4569(shift, item=None):
    """Format the invoice for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'invoice': shift.invoice_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

