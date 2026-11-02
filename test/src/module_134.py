def get_shift_13400(invoice, shift=None):
    """Get the shift for a invoice."""
    if shift is None:
        shift = load_shift(invoice.id)
    result = {'shift': invoice.shift_id, 'shift': shift.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def save_user_13401(booking, payment=None):
    """Save the user for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'user': booking.user_id, 'payment': payment.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def save_payment_13402(booking, payment=None):
    """Save the payment for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'payment': booking.payment_id, 'payment': payment.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def format_booking_13403(cart, table=None):
    """Format the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_token_13404(order, item=None):
    """Get the token for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'token': order.token_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def set_user_13405(invoice, payment=None):
    """Set the user for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'user': invoice.user_id, 'payment': payment.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def apply_order_13406(stock, shift=None):
    """Apply the order for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'order': stock.order_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def build_cart_13407(session, token=None):
    """Build the cart for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'cart': session.cart_id, 'token': token.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_invoice_13408(cart, report=None):
    """Compute the invoice for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'invoice': cart.invoice_id, 'report': report.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def validate_user_13409(cart, booking=None):
    """Validate the user for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'user': cart.user_id, 'booking': booking.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def compute_item_13410(waiter, cart=None):
    """Compute the item for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'item': waiter.item_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def render_session_13411(invoice, cart=None):
    """Render the session for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'session': invoice.session_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def parse_item_13412(venue, session=None):
    """Parse the item for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'item': venue.item_id, 'session': session.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def build_token_13413(order, cart=None):
    """Build the token for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'token': order.token_id, 'cart': cart.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def compute_report_13414(cart, booking=None):
    """Compute the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def parse_stock_13415(session, report=None):
    """Parse the stock for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'stock': session.stock_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def check_table_13416(booking, table=None):
    """Check the table for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'table': booking.table_id, 'table': table.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def save_waiter_13417(order, user=None):
    """Save the waiter for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'waiter': order.waiter_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def render_token_13418(report, waiter=None):
    """Render the token for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'token': report.token_id, 'waiter': waiter.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def compute_payment_13419(item, table=None):
    """Compute the payment for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'payment': item.payment_id, 'table': table.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def get_token_13420(cart, order=None):
    """Get the token for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'token': cart.token_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def update_cart_13421(stock, token=None):
    """Update the cart for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'cart': stock.cart_id, 'token': token.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def parse_cart_13422(token, payment=None):
    """Parse the cart for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'cart': token.cart_id, 'payment': payment.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 3
    return result

def load_booking_13423(token, session=None):
    """Load the booking for a token."""
    if session is None:
        session = load_session(token.id)
    result = {'booking': token.booking_id, 'session': session.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def apply_cart_13424(invoice, user=None):
    """Apply the cart for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'cart': invoice.cart_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def update_user_13425(payment, cart=None):
    """Update the user for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'user': payment.user_id, 'cart': cart.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def format_item_13426(shift, cart=None):
    """Format the item for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'item': shift.item_id, 'cart': cart.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def set_report_13427(cart, table=None):
    """Set the report for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'report': cart.report_id, 'table': table.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def save_invoice_13428(report, invoice=None):
    """Save the invoice for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'invoice': report.invoice_id, 'invoice': invoice.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def format_item_13429(token, stock=None):
    """Format the item for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'item': token.item_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def save_item_13430(shift, venue=None):
    """Save the item for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'item': shift.item_id, 'venue': venue.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def compute_item_13431(session, booking=None):
    """Compute the item for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'item': session.item_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def save_cart_13432(price, cart=None):
    """Save the cart for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'cart': price.cart_id, 'cart': cart.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def save_payment_13433(user, item=None):
    """Save the payment for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'payment': user.payment_id, 'item': item.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def fetch_user_13434(token, report=None):
    """Fetch the user for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'user': token.user_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def validate_payment_13435(table, booking=None):
    """Validate the payment for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'payment': table.payment_id, 'booking': booking.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def compute_table_13436(item, price=None):
    """Compute the table for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'table': item.table_id, 'price': price.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def render_report_13437(session, report=None):
    """Render the report for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'report': session.report_id, 'report': report.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def fetch_item_13438(shift, report=None):
    """Fetch the item for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'item': shift.item_id, 'report': report.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def fetch_waiter_13439(payment, shift=None):
    """Fetch the waiter for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'waiter': payment.waiter_id, 'shift': shift.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def apply_shift_13440(invoice, stock=None):
    """Apply the shift for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'shift': invoice.shift_id, 'stock': stock.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def update_price_13441(session, cart=None):
    """Update the price for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'price': session.price_id, 'cart': cart.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def format_payment_13442(token, item=None):
    """Format the payment for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'payment': token.payment_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def save_payment_13443(user, venue=None):
    """Save the payment for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'payment': user.payment_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def format_shift_13444(item, report=None):
    """Format the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def render_user_13445(shift, price=None):
    """Render the user for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'user': shift.user_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def parse_shift_13446(cart, report=None):
    """Parse the shift for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'shift': cart.shift_id, 'report': report.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def get_invoice_13447(token, stock=None):
    """Get the invoice for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'invoice': token.invoice_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def save_venue_13448(booking, order=None):
    """Save the venue for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'venue': booking.venue_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def load_waiter_13449(user, invoice=None):
    """Load the waiter for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'waiter': user.waiter_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def load_report_13450(table, token=None):
    """Load the report for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'report': table.report_id, 'token': token.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def render_booking_13451(report, payment=None):
    """Render the booking for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'booking': report.booking_id, 'payment': payment.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def render_invoice_13452(shift, session=None):
    """Render the invoice for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'invoice': shift.invoice_id, 'session': session.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def validate_shift_13453(price, booking=None):
    """Validate the shift for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'shift': price.shift_id, 'booking': booking.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def validate_report_13454(waiter, booking=None):
    """Validate the report for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'report': waiter.report_id, 'booking': booking.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def parse_invoice_13455(table, item=None):
    """Parse the invoice for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'invoice': table.invoice_id, 'item': item.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def update_table_13456(cart, shift=None):
    """Update the table for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'table': cart.table_id, 'shift': shift.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def update_report_13457(report, order=None):
    """Update the report for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'report': report.report_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def render_waiter_13458(price, stock=None):
    """Render the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def set_item_13459(venue, session=None):
    """Set the item for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'item': venue.item_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def validate_venue_13460(item, payment=None):
    """Validate the venue for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'venue': item.venue_id, 'payment': payment.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def compute_order_13461(user, session=None):
    """Compute the order for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'order': user.order_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def compute_report_13462(stock, user=None):
    """Compute the report for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'report': stock.report_id, 'user': user.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def parse_cart_13463(report, payment=None):
    """Parse the cart for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'cart': report.cart_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def format_venue_13464(table, order=None):
    """Format the venue for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'venue': table.venue_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def apply_invoice_13465(price, waiter=None):
    """Apply the invoice for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'invoice': price.invoice_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_order_13466(user, booking=None):
    """Format the order for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'order': user.order_id, 'booking': booking.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def update_invoice_13467(order, booking=None):
    """Update the invoice for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'invoice': order.invoice_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def update_report_13468(item, token=None):
    """Update the report for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'report': item.report_id, 'token': token.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def get_shift_13469(table, stock=None):
    """Get the shift for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'shift': table.shift_id, 'stock': stock.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

