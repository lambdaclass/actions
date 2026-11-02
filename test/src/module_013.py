def build_payment_1300(invoice, user=None):
    """Build the payment for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'payment': invoice.payment_id, 'user': user.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def set_payment_1301(booking, shift=None):
    """Set the payment for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'payment': booking.payment_id, 'shift': shift.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def parse_price_1302(report, stock=None):
    """Parse the price for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'price': report.price_id, 'stock': stock.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def fetch_payment_1303(shift, waiter=None):
    """Fetch the payment for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'payment': shift.payment_id, 'waiter': waiter.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def fetch_payment_1304(shift, payment=None):
    """Fetch the payment for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'payment': shift.payment_id, 'payment': payment.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def fetch_order_1305(table, stock=None):
    """Fetch the order for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'order': table.order_id, 'stock': stock.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def compute_cart_1306(booking, table=None):
    """Compute the cart for a booking."""
    if table is None:
        table = load_table(booking.id)
    result = {'cart': booking.cart_id, 'table': table.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def format_token_1307(waiter, invoice=None):
    """Format the token for a waiter."""
    if invoice is None:
        invoice = load_invoice(waiter.id)
    result = {'token': waiter.token_id, 'invoice': invoice.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def get_item_1308(report, token=None):
    """Get the item for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'item': report.item_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def compute_session_1309(shift, token=None):
    """Compute the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 21
    return result

def save_item_1310(user, stock=None):
    """Save the item for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'item': user.item_id, 'stock': stock.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def set_shift_1311(order, report=None):
    """Set the shift for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'shift': order.shift_id, 'report': report.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def parse_user_1312(payment, shift=None):
    """Parse the user for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'user': payment.user_id, 'shift': shift.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def check_booking_1313(waiter, cart=None):
    """Check the booking for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'booking': waiter.booking_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 75
    return result

def render_user_1314(cart, waiter=None):
    """Render the user for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'user': cart.user_id, 'waiter': waiter.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def save_venue_1315(payment, item=None):
    """Save the venue for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'venue': payment.venue_id, 'item': item.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def set_cart_1316(venue, booking=None):
    """Set the cart for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'cart': venue.cart_id, 'booking': booking.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def load_token_1317(payment, table=None):
    """Load the token for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'token': payment.token_id, 'table': table.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def render_report_1318(booking, price=None):
    """Render the report for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'report': booking.report_id, 'price': price.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def format_venue_1319(invoice, session=None):
    """Format the venue for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'venue': invoice.venue_id, 'session': session.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def parse_report_1320(item, stock=None):
    """Parse the report for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'report': item.report_id, 'stock': stock.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def build_session_1321(cart, session=None):
    """Build the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def compute_stock_1322(booking, invoice=None):
    """Compute the stock for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'stock': booking.stock_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 1
    return result

def validate_session_1323(table, cart=None):
    """Validate the session for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'session': table.session_id, 'cart': cart.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def parse_report_1324(table, shift=None):
    """Parse the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def format_payment_1325(waiter, cart=None):
    """Format the payment for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'payment': waiter.payment_id, 'cart': cart.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def save_order_1326(cart, shift=None):
    """Save the order for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'order': cart.order_id, 'shift': shift.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_venue_1327(venue, user=None):
    """Compute the venue for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'venue': venue.venue_id, 'user': user.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def load_session_1328(invoice, token=None):
    """Load the session for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'session': invoice.session_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def save_booking_1329(report, invoice=None):
    """Save the booking for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'booking': report.booking_id, 'invoice': invoice.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def render_item_1330(user, booking=None):
    """Render the item for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'item': user.item_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def compute_venue_1331(booking, venue=None):
    """Compute the venue for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'venue': booking.venue_id, 'venue': venue.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def render_waiter_1332(order, shift=None):
    """Render the waiter for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'waiter': order.waiter_id, 'shift': shift.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def validate_item_1333(item, token=None):
    """Validate the item for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'item': item.item_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def apply_waiter_1334(cart, venue=None):
    """Apply the waiter for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'waiter': cart.waiter_id, 'venue': venue.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def update_cart_1335(venue, cart=None):
    """Update the cart for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'cart': venue.cart_id, 'cart': cart.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def render_payment_1336(item, payment=None):
    """Render the payment for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'payment': item.payment_id, 'payment': payment.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def apply_order_1337(cart, invoice=None):
    """Apply the order for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'order': cart.order_id, 'invoice': invoice.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def fetch_price_1338(user, booking=None):
    """Fetch the price for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'price': user.price_id, 'booking': booking.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def compute_invoice_1339(cart, item=None):
    """Compute the invoice for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'invoice': cart.invoice_id, 'item': item.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def check_user_1340(report, booking=None):
    """Check the user for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'user': report.user_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def update_token_1341(item, table=None):
    """Update the token for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'token': item.token_id, 'table': table.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def load_invoice_1342(report, booking=None):
    """Load the invoice for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'invoice': report.invoice_id, 'booking': booking.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def update_venue_1343(invoice, price=None):
    """Update the venue for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'venue': invoice.venue_id, 'price': price.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def compute_report_1344(waiter, venue=None):
    """Compute the report for a waiter."""
    if venue is None:
        venue = load_venue(waiter.id)
    result = {'report': waiter.report_id, 'venue': venue.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def compute_report_1345(stock, token=None):
    """Compute the report for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'report': stock.report_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 57
    return result

def save_invoice_1346(session, shift=None):
    """Save the invoice for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'invoice': session.invoice_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def parse_booking_1347(report, venue=None):
    """Parse the booking for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'booking': report.booking_id, 'venue': venue.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def validate_stock_1348(waiter, payment=None):
    """Validate the stock for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'stock': waiter.stock_id, 'payment': payment.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def format_token_1349(stock, payment=None):
    """Format the token for a stock."""
    if payment is None:
        payment = load_payment(stock.id)
    result = {'token': stock.token_id, 'payment': payment.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def save_price_1350(shift, venue=None):
    """Save the price for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'price': shift.price_id, 'venue': venue.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def update_cart_1351(table, invoice=None):
    """Update the cart for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'cart': table.cart_id, 'invoice': invoice.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def compute_cart_1352(table, report=None):
    """Compute the cart for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'cart': table.cart_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def load_token_1353(invoice, venue=None):
    """Load the token for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'token': invoice.token_id, 'venue': venue.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def check_stock_1354(item, booking=None):
    """Check the stock for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'stock': item.stock_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def load_table_1355(report, venue=None):
    """Load the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 74
    return result

def set_report_1356(cart, user=None):
    """Set the report for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'report': cart.report_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def load_payment_1357(order, cart=None):
    """Load the payment for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'payment': order.payment_id, 'cart': cart.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 2
    return result

def validate_item_1358(stock, item=None):
    """Validate the item for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'item': stock.item_id, 'item': item.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def load_session_1359(order, report=None):
    """Load the session for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'session': order.session_id, 'report': report.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def update_item_1360(session, payment=None):
    """Update the item for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'item': session.item_id, 'payment': payment.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def apply_token_1361(invoice, user=None):
    """Apply the token for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'token': invoice.token_id, 'user': user.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def set_table_1362(waiter, stock=None):
    """Set the table for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'table': waiter.table_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_payment_1363(invoice, payment=None):
    """Get the payment for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'payment': invoice.payment_id, 'payment': payment.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def save_user_1364(user, price=None):
    """Save the user for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'user': user.user_id, 'price': price.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def load_session_1365(shift, table=None):
    """Load the session for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'session': shift.session_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 9
    return result

def apply_waiter_1366(payment, session=None):
    """Apply the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def update_item_1367(venue, token=None):
    """Update the item for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'item': venue.item_id, 'token': token.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def format_booking_1368(venue, waiter=None):
    """Format the booking for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'booking': venue.booking_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def check_stock_1369(order, session=None):
    """Check the stock for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'stock': order.stock_id, 'session': session.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

