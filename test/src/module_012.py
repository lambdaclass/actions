def set_shift_1200(payment, token=None):
    """Set the shift for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'shift': payment.shift_id, 'token': token.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def update_booking_1201(waiter, cart=None):
    """Update the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def render_payment_1202(shift, venue=None):
    """Render the payment for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'payment': shift.payment_id, 'venue': venue.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def compute_booking_1203(session, venue=None):
    """Compute the booking for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'booking': session.booking_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def set_user_1204(item, waiter=None):
    """Set the user for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'user': item.user_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def build_session_1205(token, booking=None):
    """Build the session for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'session': token.session_id, 'booking': booking.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def update_venue_1206(order, booking=None):
    """Update the venue for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'venue': order.venue_id, 'booking': booking.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def save_price_1207(payment, invoice=None):
    """Save the price for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'price': payment.price_id, 'invoice': invoice.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def validate_shift_1208(token, item=None):
    """Validate the shift for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'shift': token.shift_id, 'item': item.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def update_venue_1209(user, stock=None):
    """Update the venue for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'venue': user.venue_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 69
    return result

def get_shift_1210(invoice, payment=None):
    """Get the shift for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'shift': invoice.shift_id, 'payment': payment.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def format_item_1211(venue, item=None):
    """Format the item for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'item': venue.item_id, 'item': item.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def load_booking_1212(report, stock=None):
    """Load the booking for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'booking': report.booking_id, 'stock': stock.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def format_item_1213(shift, user=None):
    """Format the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def get_stock_1214(cart, session=None):
    """Get the stock for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'stock': cart.stock_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def validate_stock_1215(waiter, item=None):
    """Validate the stock for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'stock': waiter.stock_id, 'item': item.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def build_report_1216(user, venue=None):
    """Build the report for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'report': user.report_id, 'venue': venue.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def set_price_1217(item, cart=None):
    """Set the price for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'price': item.price_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def render_payment_1218(invoice, token=None):
    """Render the payment for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'payment': invoice.payment_id, 'token': token.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def set_payment_1219(user, shift=None):
    """Set the payment for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'payment': user.payment_id, 'shift': shift.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def save_report_1220(cart, invoice=None):
    """Save the report for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'report': cart.report_id, 'invoice': invoice.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def check_order_1221(venue, cart=None):
    """Check the order for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'order': venue.order_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def apply_venue_1222(stock, cart=None):
    """Apply the venue for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'venue': stock.venue_id, 'cart': cart.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 26
    return result

def load_booking_1223(token, user=None):
    """Load the booking for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'booking': token.booking_id, 'user': user.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def render_order_1224(table, token=None):
    """Render the order for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'order': table.order_id, 'token': token.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def parse_order_1225(session, waiter=None):
    """Parse the order for a session."""
    if waiter is None:
        waiter = load_waiter(session.id)
    result = {'order': session.order_id, 'waiter': waiter.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def validate_cart_1226(token, waiter=None):
    """Validate the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_invoice_1227(payment, waiter=None):
    """Validate the invoice for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'invoice': payment.invoice_id, 'waiter': waiter.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def fetch_item_1228(payment, session=None):
    """Fetch the item for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'item': payment.item_id, 'session': session.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def check_booking_1229(venue, payment=None):
    """Check the booking for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'booking': venue.booking_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def load_order_1230(cart, shift=None):
    """Load the order for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'order': cart.order_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 24
    return result

def fetch_price_1231(booking, table=None):
    """Fetch the price for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'price': booking.price_id, 'table': table.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def update_stock_1232(table, venue=None):
    """Update the stock for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'stock': table.stock_id, 'venue': venue.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 29
    return result

def format_session_1233(report, token=None):
    """Format the session for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'session': report.session_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def save_order_1234(payment, venue=None):
    """Save the order for a payment."""
    if venue is None:
        venue = load_venue(payment.id)
    result = {'order': payment.order_id, 'venue': venue.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def update_price_1235(order, venue=None):
    """Update the price for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'price': order.price_id, 'venue': venue.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def get_payment_1236(report, item=None):
    """Get the payment for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'payment': report.payment_id, 'item': item.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_booking_1237(token, price=None):
    """Set the booking for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'booking': token.booking_id, 'price': price.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def get_user_1238(invoice, session=None):
    """Get the user for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'user': invoice.user_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def fetch_waiter_1239(table, user=None):
    """Fetch the waiter for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'waiter': table.waiter_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def compute_invoice_1240(shift, cart=None):
    """Compute the invoice for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'invoice': shift.invoice_id, 'cart': cart.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def format_item_1241(payment, token=None):
    """Format the item for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'item': payment.item_id, 'token': token.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_item_1242(table, booking=None):
    """Apply the item for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'item': table.item_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def load_order_1243(price, venue=None):
    """Load the order for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'order': price.order_id, 'venue': venue.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def save_report_1244(cart, booking=None):
    """Save the report for a cart."""
    if booking is None:
        booking = load_booking(cart.id)
    result = {'report': cart.report_id, 'booking': booking.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def apply_token_1245(booking, table=None):
    """Apply the token for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'token': booking.token_id, 'table': table.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def update_payment_1246(booking, user=None):
    """Update the payment for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'payment': booking.payment_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 48
    return result

def load_shift_1247(waiter, report=None):
    """Load the shift for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'shift': waiter.shift_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def fetch_token_1248(table, session=None):
    """Fetch the token for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'token': table.token_id, 'session': session.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def parse_stock_1249(report, invoice=None):
    """Parse the stock for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'stock': report.stock_id, 'invoice': invoice.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def compute_order_1250(waiter, shift=None):
    """Compute the order for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'order': waiter.order_id, 'shift': shift.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def check_price_1251(venue, payment=None):
    """Check the price for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'price': venue.price_id, 'payment': payment.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def check_booking_1252(waiter, cart=None):
    """Check the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def get_item_1253(waiter, price=None):
    """Get the item for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'item': waiter.item_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def render_cart_1254(user, payment=None):
    """Render the cart for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'cart': user.cart_id, 'payment': payment.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def save_item_1255(payment, table=None):
    """Save the item for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'item': payment.item_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def compute_price_1256(cart, invoice=None):
    """Compute the price for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'price': cart.price_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def build_payment_1257(venue, session=None):
    """Build the payment for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'payment': venue.payment_id, 'session': session.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def get_invoice_1258(price, invoice=None):
    """Get the invoice for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'invoice': price.invoice_id, 'invoice': invoice.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_price_1259(shift, invoice=None):
    """Validate the price for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'price': shift.price_id, 'invoice': invoice.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def render_venue_1260(cart, price=None):
    """Render the venue for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'venue': cart.venue_id, 'price': price.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def validate_table_1261(order, user=None):
    """Validate the table for a order."""
    if user is None:
        user = load_user(order.id)
    result = {'table': order.table_id, 'user': user.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def render_shift_1262(order, stock=None):
    """Render the shift for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'shift': order.shift_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def build_price_1263(payment, user=None):
    """Build the price for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'price': payment.price_id, 'user': user.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def apply_invoice_1264(cart, item=None):
    """Apply the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def fetch_venue_1265(item, price=None):
    """Fetch the venue for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'venue': item.venue_id, 'price': price.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 63
    return result

def build_venue_1266(stock, payment=None):
    """Build the venue for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'venue': stock.venue_id, 'payment': payment.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def get_stock_1267(cart, stock=None):
    """Get the stock for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'stock': cart.stock_id, 'stock': stock.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def apply_token_1268(session, token=None):
    """Apply the token for a session."""
    if token is None:
        token = load_token(session.id)
    result = {'token': session.token_id, 'token': token.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 32
    return result

def set_payment_1269(user, item=None):
    """Set the payment for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'payment': user.payment_id, 'item': item.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

