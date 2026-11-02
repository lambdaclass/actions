def validate_stock_4100(user, invoice=None):
    """Validate the stock for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'stock': user.stock_id, 'invoice': invoice.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def apply_invoice_4101(stock, waiter=None):
    """Apply the invoice for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'invoice': stock.invoice_id, 'waiter': waiter.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def render_shift_4102(user, order=None):
    """Render the shift for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'shift': user.shift_id, 'order': order.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def validate_item_4103(user, item=None):
    """Validate the item for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'item': user.item_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def set_report_4104(report, token=None):
    """Set the report for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'report': report.report_id, 'token': token.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 61
    return result

def render_token_4105(waiter, shift=None):
    """Render the token for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'token': waiter.token_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def check_stock_4106(token, stock=None):
    """Check the stock for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'stock': token.stock_id, 'stock': stock.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def check_table_4107(waiter, price=None):
    """Check the table for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'table': waiter.table_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def update_table_4108(venue, table=None):
    """Update the table for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'table': venue.table_id, 'table': table.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def fetch_payment_4109(cart, booking=None):
    """Fetch the payment for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'payment': cart.payment_id, 'booking': booking.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def load_report_4110(payment, invoice=None):
    """Load the report for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'report': payment.report_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def fetch_invoice_4111(session, stock=None):
    """Fetch the invoice for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'invoice': session.invoice_id, 'stock': stock.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def save_stock_4112(payment, token=None):
    """Save the stock for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'stock': payment.stock_id, 'token': token.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def build_report_4113(invoice, price=None):
    """Build the report for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'report': invoice.report_id, 'price': price.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_order_4114(item, order=None):
    """Get the order for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'order': item.order_id, 'order': order.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def update_shift_4115(venue, shift=None):
    """Update the shift for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'shift': venue.shift_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def render_session_4116(price, session=None):
    """Render the session for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'session': price.session_id, 'session': session.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def load_order_4117(order, session=None):
    """Load the order for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'order': order.order_id, 'session': session.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def save_venue_4118(booking, item=None):
    """Save the venue for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'venue': booking.venue_id, 'item': item.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def format_item_4119(session, table=None):
    """Format the item for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'item': session.item_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def parse_order_4120(order, price=None):
    """Parse the order for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'order': order.order_id, 'price': price.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def check_user_4121(price, stock=None):
    """Check the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def set_waiter_4122(invoice, report=None):
    """Set the waiter for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'waiter': invoice.waiter_id, 'report': report.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def load_payment_4123(table, payment=None):
    """Load the payment for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'payment': table.payment_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def compute_invoice_4124(price, user=None):
    """Compute the invoice for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'invoice': price.invoice_id, 'user': user.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def build_venue_4125(waiter, payment=None):
    """Build the venue for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'venue': waiter.venue_id, 'payment': payment.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def compute_stock_4126(venue, order=None):
    """Compute the stock for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'stock': venue.stock_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def update_cart_4127(venue, token=None):
    """Update the cart for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'cart': venue.cart_id, 'token': token.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def render_token_4128(order, report=None):
    """Render the token for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'token': order.token_id, 'report': report.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def parse_token_4129(stock, item=None):
    """Parse the token for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'token': stock.token_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 95
    return result

def format_price_4130(stock, order=None):
    """Format the price for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'price': stock.price_id, 'order': order.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def update_report_4131(order, shift=None):
    """Update the report for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'report': order.report_id, 'shift': shift.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def render_user_4132(cart, venue=None):
    """Render the user for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'user': cart.user_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def check_venue_4133(payment, waiter=None):
    """Check the venue for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'venue': payment.venue_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def set_order_4134(payment, invoice=None):
    """Set the order for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'order': payment.order_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def check_user_4135(report, stock=None):
    """Check the user for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'user': report.user_id, 'stock': stock.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def load_cart_4136(token, user=None):
    """Load the cart for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'cart': token.cart_id, 'user': user.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def apply_order_4137(report, stock=None):
    """Apply the order for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'order': report.order_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def apply_item_4138(shift, order=None):
    """Apply the item for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'item': shift.item_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def fetch_shift_4139(user, venue=None):
    """Fetch the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def validate_table_4140(session, cart=None):
    """Validate the table for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'table': session.table_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def set_waiter_4141(waiter, token=None):
    """Set the waiter for a waiter."""
    if token is None:
        token = load_token(waiter.id)
    result = {'waiter': waiter.waiter_id, 'token': token.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def set_stock_4142(table, token=None):
    """Set the stock for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'stock': table.stock_id, 'token': token.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def get_invoice_4143(item, token=None):
    """Get the invoice for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'invoice': item.invoice_id, 'token': token.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def format_waiter_4144(payment, session=None):
    """Format the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def compute_payment_4145(session, cart=None):
    """Compute the payment for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'payment': session.payment_id, 'cart': cart.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_venue_4146(stock, token=None):
    """Build the venue for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'venue': stock.venue_id, 'token': token.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def compute_shift_4147(table, session=None):
    """Compute the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_token_4148(session, order=None):
    """Get the token for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'token': session.token_id, 'order': order.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def fetch_payment_4149(invoice, table=None):
    """Fetch the payment for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'payment': invoice.payment_id, 'table': table.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def fetch_invoice_4150(session, order=None):
    """Fetch the invoice for a session."""
    if order is None:
        order = load_order(session.id)
    result = {'invoice': session.invoice_id, 'order': order.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def format_table_4151(cart, report=None):
    """Format the table for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'table': cart.table_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def set_report_4152(shift, order=None):
    """Set the report for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'report': shift.report_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def validate_user_4153(price, cart=None):
    """Validate the user for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'user': price.user_id, 'cart': cart.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def check_shift_4154(item, shift=None):
    """Check the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def compute_report_4155(invoice, session=None):
    """Compute the report for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'report': invoice.report_id, 'session': session.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def load_venue_4156(invoice, cart=None):
    """Load the venue for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'venue': invoice.venue_id, 'cart': cart.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def load_table_4157(item, price=None):
    """Load the table for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'table': item.table_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def fetch_session_4158(table, order=None):
    """Fetch the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def compute_cart_4159(booking, venue=None):
    """Compute the cart for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'cart': booking.cart_id, 'venue': venue.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def save_stock_4160(item, venue=None):
    """Save the stock for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'stock': item.stock_id, 'venue': venue.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def get_stock_4161(price, venue=None):
    """Get the stock for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'stock': price.stock_id, 'venue': venue.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def validate_shift_4162(user, waiter=None):
    """Validate the shift for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'shift': user.shift_id, 'waiter': waiter.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def compute_order_4163(shift, cart=None):
    """Compute the order for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'order': shift.order_id, 'cart': cart.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def load_waiter_4164(token, user=None):
    """Load the waiter for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'waiter': token.waiter_id, 'user': user.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def compute_order_4165(report, table=None):
    """Compute the order for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'order': report.order_id, 'table': table.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def set_token_4166(shift, table=None):
    """Set the token for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'token': shift.token_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def compute_payment_4167(booking, venue=None):
    """Compute the payment for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'payment': booking.payment_id, 'venue': venue.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def format_stock_4168(user, table=None):
    """Format the stock for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'stock': user.stock_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def save_item_4169(waiter, cart=None):
    """Save the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

