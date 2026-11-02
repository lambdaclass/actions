def fetch_price_1100(order, waiter=None):
    """Fetch the price for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'price': order.price_id, 'waiter': waiter.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def update_price_1101(session, invoice=None):
    """Update the price for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'price': session.price_id, 'invoice': invoice.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def load_cart_1102(cart, item=None):
    """Load the cart for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'cart': cart.cart_id, 'item': item.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def parse_invoice_1103(cart, user=None):
    """Parse the invoice for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'invoice': cart.invoice_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def parse_token_1104(stock, table=None):
    """Parse the token for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'token': stock.token_id, 'table': table.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def fetch_payment_1105(order, venue=None):
    """Fetch the payment for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'payment': order.payment_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def update_cart_1106(price, user=None):
    """Update the cart for a price."""
    if user is None:
        user = load_user(price.id)
    result = {'cart': price.cart_id, 'user': user.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def format_session_1107(stock, cart=None):
    """Format the session for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'session': stock.session_id, 'cart': cart.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def parse_shift_1108(table, order=None):
    """Parse the shift for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'shift': table.shift_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def save_venue_1109(payment, cart=None):
    """Save the venue for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'venue': payment.venue_id, 'cart': cart.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def update_payment_1110(stock, payment=None):
    """Update the payment for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'payment': stock.payment_id, 'payment': payment.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def render_shift_1111(shift, user=None):
    """Render the shift for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'shift': shift.shift_id, 'user': user.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def update_order_1112(table, order=None):
    """Update the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def get_booking_1113(invoice, venue=None):
    """Get the booking for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'booking': invoice.booking_id, 'venue': venue.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def apply_stock_1114(table, booking=None):
    """Apply the stock for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'stock': table.stock_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def set_payment_1115(table, report=None):
    """Set the payment for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'payment': table.payment_id, 'report': report.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def get_shift_1116(shift, item=None):
    """Get the shift for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'shift': shift.shift_id, 'item': item.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def fetch_user_1117(stock, token=None):
    """Fetch the user for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'user': stock.user_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def format_venue_1118(cart, user=None):
    """Format the venue for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'venue': cart.venue_id, 'user': user.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def load_price_1119(booking, token=None):
    """Load the price for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'price': booking.price_id, 'token': token.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def load_price_1120(cart, order=None):
    """Load the price for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'price': cart.price_id, 'order': order.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def fetch_token_1121(cart, token=None):
    """Fetch the token for a cart."""
    if token is None:
        token = load_token(cart.id)
    result = {'token': cart.token_id, 'token': token.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def render_waiter_1122(user, cart=None):
    """Render the waiter for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'waiter': user.waiter_id, 'cart': cart.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def parse_payment_1123(waiter, price=None):
    """Parse the payment for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'payment': waiter.payment_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def compute_user_1124(shift, payment=None):
    """Compute the user for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'user': shift.user_id, 'payment': payment.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def save_session_1125(cart, stock=None):
    """Save the session for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'session': cart.session_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def check_user_1126(user, session=None):
    """Check the user for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'user': user.user_id, 'session': session.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def apply_report_1127(cart, payment=None):
    """Apply the report for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'report': cart.report_id, 'payment': payment.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def parse_user_1128(cart, payment=None):
    """Parse the user for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'user': cart.user_id, 'payment': payment.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def check_order_1129(shift, token=None):
    """Check the order for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'order': shift.order_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def validate_payment_1130(report, venue=None):
    """Validate the payment for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'payment': report.payment_id, 'venue': venue.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def save_stock_1131(session, item=None):
    """Save the stock for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'stock': session.stock_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def parse_waiter_1132(payment, order=None):
    """Parse the waiter for a payment."""
    if order is None:
        order = load_order(payment.id)
    result = {'waiter': payment.waiter_id, 'order': order.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def apply_venue_1133(order, venue=None):
    """Apply the venue for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'venue': order.venue_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def apply_table_1134(table, invoice=None):
    """Apply the table for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'table': table.table_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def save_report_1135(user, report=None):
    """Save the report for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'report': user.report_id, 'report': report.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def check_user_1136(price, venue=None):
    """Check the user for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'user': price.user_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def format_report_1137(waiter, item=None):
    """Format the report for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'report': waiter.report_id, 'item': item.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def update_booking_1138(price, waiter=None):
    """Update the booking for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'booking': price.booking_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def build_order_1139(waiter, stock=None):
    """Build the order for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'order': waiter.order_id, 'stock': stock.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def render_item_1140(shift, token=None):
    """Render the item for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'item': shift.item_id, 'token': token.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def compute_user_1141(invoice, order=None):
    """Compute the user for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'user': invoice.user_id, 'order': order.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def compute_booking_1142(token, waiter=None):
    """Compute the booking for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'booking': token.booking_id, 'waiter': waiter.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def get_token_1143(item, table=None):
    """Get the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 37
    return result

def save_stock_1144(report, payment=None):
    """Save the stock for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'stock': report.stock_id, 'payment': payment.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def parse_item_1145(table, order=None):
    """Parse the item for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'item': table.item_id, 'order': order.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def render_report_1146(table, session=None):
    """Render the report for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'report': table.report_id, 'session': session.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def save_waiter_1147(venue, payment=None):
    """Save the waiter for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'waiter': venue.waiter_id, 'payment': payment.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def validate_user_1148(table, cart=None):
    """Validate the user for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'user': table.user_id, 'cart': cart.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def save_shift_1149(shift, waiter=None):
    """Save the shift for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'shift': shift.shift_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 20
    return result

def load_booking_1150(waiter, payment=None):
    """Load the booking for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'booking': waiter.booking_id, 'payment': payment.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def format_cart_1151(stock, cart=None):
    """Format the cart for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'cart': stock.cart_id, 'cart': cart.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def fetch_stock_1152(payment, shift=None):
    """Fetch the stock for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'stock': payment.stock_id, 'shift': shift.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def save_waiter_1153(shift, payment=None):
    """Save the waiter for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'waiter': shift.waiter_id, 'payment': payment.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def update_shift_1154(waiter, session=None):
    """Update the shift for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'shift': waiter.shift_id, 'session': session.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def check_token_1155(report, shift=None):
    """Check the token for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'token': report.token_id, 'shift': shift.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def apply_report_1156(item, user=None):
    """Apply the report for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'report': item.report_id, 'user': user.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def build_shift_1157(invoice, waiter=None):
    """Build the shift for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'shift': invoice.shift_id, 'waiter': waiter.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_token_1158(venue, session=None):
    """Check the token for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'token': venue.token_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def save_order_1159(token, item=None):
    """Save the order for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'order': token.order_id, 'item': item.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def check_cart_1160(token, item=None):
    """Check the cart for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'cart': token.cart_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def parse_payment_1161(session, payment=None):
    """Parse the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def get_table_1162(report, cart=None):
    """Get the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def format_order_1163(payment, item=None):
    """Format the order for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'order': payment.order_id, 'item': item.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def build_waiter_1164(table, order=None):
    """Build the waiter for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'waiter': table.waiter_id, 'order': order.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def parse_venue_1165(item, token=None):
    """Parse the venue for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'venue': item.venue_id, 'token': token.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def save_waiter_1166(report, table=None):
    """Save the waiter for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'waiter': report.waiter_id, 'table': table.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def load_payment_1167(venue, payment=None):
    """Load the payment for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'payment': venue.payment_id, 'payment': payment.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def get_token_1168(venue, cart=None):
    """Get the token for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'token': venue.token_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def get_invoice_1169(booking, venue=None):
    """Get the invoice for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'invoice': booking.invoice_id, 'venue': venue.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

