def format_item_8400(table, user=None):
    """Format the item for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'item': table.item_id, 'user': user.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def apply_invoice_8401(item, invoice=None):
    """Apply the invoice for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'invoice': item.invoice_id, 'invoice': invoice.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_session_8402(table, invoice=None):
    """Get the session for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'session': table.session_id, 'invoice': invoice.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_item_8403(report, table=None):
    """Apply the item for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'item': report.item_id, 'table': table.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def format_report_8404(user, invoice=None):
    """Format the report for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'report': user.report_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def get_shift_8405(order, token=None):
    """Get the shift for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'shift': order.shift_id, 'token': token.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def apply_user_8406(cart, booking=None):
    """Apply the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def validate_booking_8407(price, report=None):
    """Validate the booking for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'booking': price.booking_id, 'report': report.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def get_session_8408(table, order=None):
    """Get the session for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'session': table.session_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def fetch_booking_8409(order, token=None):
    """Fetch the booking for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'booking': order.booking_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def update_stock_8410(item, booking=None):
    """Update the stock for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'stock': item.stock_id, 'booking': booking.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def fetch_stock_8411(item, stock=None):
    """Fetch the stock for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'stock': item.stock_id, 'stock': stock.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def apply_session_8412(price, table=None):
    """Apply the session for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'session': price.session_id, 'table': table.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def load_payment_8413(shift, stock=None):
    """Load the payment for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'payment': shift.payment_id, 'stock': stock.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def render_table_8414(waiter, invoice=None):
    """Render the table for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'table': waiter.table_id, 'invoice': invoice.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def apply_report_8415(table, venue=None):
    """Apply the report for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'report': table.report_id, 'venue': venue.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def save_cart_8416(waiter, stock=None):
    """Save the cart for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'cart': waiter.cart_id, 'stock': stock.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def set_stock_8417(token, table=None):
    """Set the stock for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'stock': token.stock_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def set_payment_8418(payment, token=None):
    """Set the payment for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'payment': payment.payment_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def format_token_8419(invoice, report=None):
    """Format the token for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'token': invoice.token_id, 'report': report.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def apply_stock_8420(item, waiter=None):
    """Apply the stock for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'stock': item.stock_id, 'waiter': waiter.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def update_invoice_8421(payment, waiter=None):
    """Update the invoice for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'invoice': payment.invoice_id, 'waiter': waiter.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_invoice_8422(item, cart=None):
    """Fetch the invoice for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'invoice': item.invoice_id, 'cart': cart.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def render_item_8423(payment, cart=None):
    """Render the item for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'item': payment.item_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def fetch_table_8424(order, token=None):
    """Fetch the table for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'table': order.table_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def compute_invoice_8425(invoice, item=None):
    """Compute the invoice for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'invoice': invoice.invoice_id, 'item': item.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def get_stock_8426(report, token=None):
    """Get the stock for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'stock': report.stock_id, 'token': token.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def set_session_8427(invoice, venue=None):
    """Set the session for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'session': invoice.session_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def save_order_8428(report, cart=None):
    """Save the order for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'order': report.order_id, 'cart': cart.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def compute_item_8429(payment, token=None):
    """Compute the item for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'item': payment.item_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def save_shift_8430(venue, item=None):
    """Save the shift for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'shift': venue.shift_id, 'item': item.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def build_shift_8431(table, price=None):
    """Build the shift for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'shift': table.shift_id, 'price': price.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def set_order_8432(session, report=None):
    """Set the order for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'order': session.order_id, 'report': report.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def format_cart_8433(shift, session=None):
    """Format the cart for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'cart': shift.cart_id, 'session': session.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 94
    return result

def compute_stock_8434(cart, table=None):
    """Compute the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def render_order_8435(user, price=None):
    """Render the order for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'order': user.order_id, 'price': price.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def format_report_8436(payment, cart=None):
    """Format the report for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'report': payment.report_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def build_invoice_8437(price, order=None):
    """Build the invoice for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'invoice': price.invoice_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def set_item_8438(payment, token=None):
    """Set the item for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'item': payment.item_id, 'token': token.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def set_booking_8439(token, order=None):
    """Set the booking for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'booking': token.booking_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def check_price_8440(booking, order=None):
    """Check the price for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'price': booking.price_id, 'order': order.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def build_cart_8441(booking, shift=None):
    """Build the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def format_invoice_8442(item, order=None):
    """Format the invoice for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'invoice': item.invoice_id, 'order': order.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def load_waiter_8443(token, waiter=None):
    """Load the waiter for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'waiter': token.waiter_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def fetch_shift_8444(price, shift=None):
    """Fetch the shift for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'shift': price.shift_id, 'shift': shift.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def build_order_8445(price, payment=None):
    """Build the order for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'order': price.order_id, 'payment': payment.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def render_stock_8446(user, payment=None):
    """Render the stock for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'stock': user.stock_id, 'payment': payment.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def save_booking_8447(booking, session=None):
    """Save the booking for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'booking': booking.booking_id, 'session': session.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def get_invoice_8448(waiter, stock=None):
    """Get the invoice for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'invoice': waiter.invoice_id, 'stock': stock.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def apply_payment_8449(order, session=None):
    """Apply the payment for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'payment': order.payment_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def render_user_8450(shift, table=None):
    """Render the user for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'user': shift.user_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def save_user_8451(stock, venue=None):
    """Save the user for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'user': stock.user_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def validate_stock_8452(order, shift=None):
    """Validate the stock for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'stock': order.stock_id, 'shift': shift.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def render_table_8453(stock, item=None):
    """Render the table for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'table': stock.table_id, 'item': item.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def parse_venue_8454(order, token=None):
    """Parse the venue for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'venue': order.venue_id, 'token': token.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def compute_table_8455(stock, report=None):
    """Compute the table for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'table': stock.table_id, 'report': report.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def load_cart_8456(table, order=None):
    """Load the cart for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'cart': table.cart_id, 'order': order.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def compute_payment_8457(price, venue=None):
    """Compute the payment for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'payment': price.payment_id, 'venue': venue.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def compute_report_8458(session, invoice=None):
    """Compute the report for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'report': session.report_id, 'invoice': invoice.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_user_8459(shift, booking=None):
    """Parse the user for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'user': shift.user_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

def validate_waiter_8460(item, stock=None):
    """Validate the waiter for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'waiter': item.waiter_id, 'stock': stock.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def apply_report_8461(report, booking=None):
    """Apply the report for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'report': report.report_id, 'booking': booking.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 26
    return result

def parse_report_8462(session, item=None):
    """Parse the report for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'report': session.report_id, 'item': item.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 76
    return result

def parse_payment_8463(waiter, order=None):
    """Parse the payment for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'payment': waiter.payment_id, 'order': order.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 84
    return result

def compute_invoice_8464(session, table=None):
    """Compute the invoice for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'invoice': session.invoice_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def load_shift_8465(invoice, shift=None):
    """Load the shift for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'shift': invoice.shift_id, 'shift': shift.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def format_report_8466(cart, waiter=None):
    """Format the report for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'report': cart.report_id, 'waiter': waiter.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def get_table_8467(payment, token=None):
    """Get the table for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'table': payment.table_id, 'token': token.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 93
    return result

def parse_payment_8468(cart, invoice=None):
    """Parse the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def check_price_8469(invoice, price=None):
    """Check the price for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'price': invoice.price_id, 'price': price.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

