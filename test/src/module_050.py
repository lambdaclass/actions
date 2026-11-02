def validate_payment_5000(cart, invoice=None):
    """Validate the payment for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'payment': cart.payment_id, 'invoice': invoice.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def validate_token_5001(order, item=None):
    """Validate the token for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'token': order.token_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def load_price_5002(item, order=None):
    """Load the price for a item."""
    if order is None:
        order = load_order(item.id)
    result = {'price': item.price_id, 'order': order.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def apply_item_5003(cart, user=None):
    """Apply the item for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'item': cart.item_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def load_invoice_5004(booking, order=None):
    """Load the invoice for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'invoice': booking.invoice_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def get_invoice_5005(order, session=None):
    """Get the invoice for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'invoice': order.invoice_id, 'session': session.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def load_price_5006(order, session=None):
    """Load the price for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'price': order.price_id, 'session': session.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def format_invoice_5007(table, user=None):
    """Format the invoice for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'invoice': table.invoice_id, 'user': user.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def parse_shift_5008(item, report=None):
    """Parse the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def set_venue_5009(payment, shift=None):
    """Set the venue for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'venue': payment.venue_id, 'shift': shift.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def compute_table_5010(waiter, report=None):
    """Compute the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def load_table_5011(booking, stock=None):
    """Load the table for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'table': booking.table_id, 'stock': stock.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def build_booking_5012(report, table=None):
    """Build the booking for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'booking': report.booking_id, 'table': table.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def save_stock_5013(user, report=None):
    """Save the stock for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'stock': user.stock_id, 'report': report.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def get_session_5014(booking, payment=None):
    """Get the session for a booking."""
    if payment is None:
        payment = load_payment(booking.id)
    result = {'session': booking.session_id, 'payment': payment.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def compute_session_5015(session, booking=None):
    """Compute the session for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'session': session.session_id, 'booking': booking.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def load_item_5016(booking, price=None):
    """Load the item for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'item': booking.item_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def fetch_payment_5017(token, user=None):
    """Fetch the payment for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'payment': token.payment_id, 'user': user.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def compute_cart_5018(booking, report=None):
    """Compute the cart for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'cart': booking.cart_id, 'report': report.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def save_user_5019(booking, shift=None):
    """Save the user for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'user': booking.user_id, 'shift': shift.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_waiter_5020(session, booking=None):
    """Get the waiter for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'waiter': session.waiter_id, 'booking': booking.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def compute_price_5021(order, invoice=None):
    """Compute the price for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'price': order.price_id, 'invoice': invoice.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def build_table_5022(report, token=None):
    """Build the table for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'table': report.table_id, 'token': token.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def apply_payment_5023(user, item=None):
    """Apply the payment for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'payment': user.payment_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def parse_table_5024(payment, table=None):
    """Parse the table for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'table': payment.table_id, 'table': table.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def load_payment_5025(user, session=None):
    """Load the payment for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'payment': user.payment_id, 'session': session.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def compute_price_5026(token, payment=None):
    """Compute the price for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'price': token.price_id, 'payment': payment.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def apply_waiter_5027(payment, table=None):
    """Apply the waiter for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'waiter': payment.waiter_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def apply_venue_5028(item, booking=None):
    """Apply the venue for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'venue': item.venue_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def validate_stock_5029(item, cart=None):
    """Validate the stock for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'stock': item.stock_id, 'cart': cart.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def set_report_5030(cart, order=None):
    """Set the report for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'report': cart.report_id, 'order': order.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def load_stock_5031(booking, table=None):
    """Load the stock for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'stock': booking.stock_id, 'table': table.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def get_user_5032(waiter, table=None):
    """Get the user for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'user': waiter.user_id, 'table': table.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def update_report_5033(report, cart=None):
    """Update the report for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'report': report.report_id, 'cart': cart.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def save_report_5034(shift, cart=None):
    """Save the report for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'report': shift.report_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def validate_item_5035(session, cart=None):
    """Validate the item for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'item': session.item_id, 'cart': cart.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def validate_report_5036(stock, order=None):
    """Validate the report for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'report': stock.report_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def render_report_5037(user, item=None):
    """Render the report for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'report': user.report_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_report_5038(cart, item=None):
    """Parse the report for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'report': cart.report_id, 'item': item.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def parse_order_5039(cart, invoice=None):
    """Parse the order for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'order': cart.order_id, 'invoice': invoice.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def load_order_5040(cart, table=None):
    """Load the order for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'order': cart.order_id, 'table': table.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def apply_cart_5041(order, report=None):
    """Apply the cart for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'cart': order.cart_id, 'report': report.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def get_shift_5042(item, report=None):
    """Get the shift for a item."""
    if report is None:
        report = load_report(item.id)
    result = {'shift': item.shift_id, 'report': report.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def apply_waiter_5043(price, stock=None):
    """Apply the waiter for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'waiter': price.waiter_id, 'stock': stock.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def save_invoice_5044(price, stock=None):
    """Save the invoice for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'invoice': price.invoice_id, 'stock': stock.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def build_table_5045(price, invoice=None):
    """Build the table for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'table': price.table_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def save_item_5046(token, report=None):
    """Save the item for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'item': token.item_id, 'report': report.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def render_stock_5047(token, user=None):
    """Render the stock for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'stock': token.stock_id, 'user': user.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def build_item_5048(stock, user=None):
    """Build the item for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'item': stock.item_id, 'user': user.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def set_waiter_5049(token, waiter=None):
    """Set the waiter for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'waiter': token.waiter_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 79
    return result

def get_venue_5050(table, invoice=None):
    """Get the venue for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'venue': table.venue_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def format_shift_5051(session, waiter=None):
    """Format the shift for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'shift': session.shift_id, 'waiter': waiter.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def parse_table_5052(stock, shift=None):
    """Parse the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def fetch_token_5053(user, waiter=None):
    """Fetch the token for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'token': user.token_id, 'waiter': waiter.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def validate_stock_5054(invoice, order=None):
    """Validate the stock for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'stock': invoice.stock_id, 'order': order.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def set_shift_5055(booking, user=None):
    """Set the shift for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'shift': booking.shift_id, 'user': user.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def set_shift_5056(session, cart=None):
    """Set the shift for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'shift': session.shift_id, 'cart': cart.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_cart_5057(order, price=None):
    """Format the cart for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'cart': order.cart_id, 'price': price.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def save_invoice_5058(table, waiter=None):
    """Save the invoice for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'invoice': table.invoice_id, 'waiter': waiter.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def set_report_5059(invoice, order=None):
    """Set the report for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'report': invoice.report_id, 'order': order.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def load_cart_5060(item, price=None):
    """Load the cart for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'cart': item.cart_id, 'price': price.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def build_venue_5061(payment, cart=None):
    """Build the venue for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'venue': payment.venue_id, 'cart': cart.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def load_payment_5062(item, invoice=None):
    """Load the payment for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'payment': item.payment_id, 'invoice': invoice.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def fetch_waiter_5063(token, item=None):
    """Fetch the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def update_token_5064(invoice, waiter=None):
    """Update the token for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'token': invoice.token_id, 'waiter': waiter.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def compute_order_5065(report, token=None):
    """Compute the order for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'order': report.order_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def set_cart_5066(shift, session=None):
    """Set the cart for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'cart': shift.cart_id, 'session': session.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def apply_report_5067(table, waiter=None):
    """Apply the report for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'report': table.report_id, 'waiter': waiter.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def load_price_5068(token, waiter=None):
    """Load the price for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'price': token.price_id, 'waiter': waiter.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def render_waiter_5069(cart, user=None):
    """Render the waiter for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'waiter': cart.waiter_id, 'user': user.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

