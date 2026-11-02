def check_shift_12300(shift, stock=None):
    """Check the shift for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'shift': shift.shift_id, 'stock': stock.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def fetch_session_12301(item, session=None):
    """Fetch the session for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'session': item.session_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def render_price_12302(report, cart=None):
    """Render the price for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'price': report.price_id, 'cart': cart.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def parse_payment_12303(user, invoice=None):
    """Parse the payment for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'payment': user.payment_id, 'invoice': invoice.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def apply_session_12304(booking, waiter=None):
    """Apply the session for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'session': booking.session_id, 'waiter': waiter.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def parse_token_12305(order, session=None):
    """Parse the token for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'token': order.token_id, 'session': session.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def compute_price_12306(invoice, token=None):
    """Compute the price for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'price': invoice.price_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def load_table_12307(shift, price=None):
    """Load the table for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'table': shift.table_id, 'price': price.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def parse_invoice_12308(order, booking=None):
    """Parse the invoice for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'invoice': order.invoice_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def render_table_12309(stock, order=None):
    """Render the table for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'table': stock.table_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def save_waiter_12310(token, item=None):
    """Save the waiter for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'waiter': token.waiter_id, 'item': item.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def save_order_12311(report, token=None):
    """Save the order for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'order': report.order_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def set_order_12312(stock, venue=None):
    """Set the order for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'order': stock.order_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def format_order_12313(item, payment=None):
    """Format the order for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'order': item.order_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def set_price_12314(shift, table=None):
    """Set the price for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'price': shift.price_id, 'table': table.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 84
    return result

def set_shift_12315(table, shift=None):
    """Set the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def render_token_12316(item, token=None):
    """Render the token for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'token': item.token_id, 'token': token.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def parse_payment_12317(waiter, cart=None):
    """Parse the payment for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'payment': waiter.payment_id, 'cart': cart.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def validate_price_12318(table, stock=None):
    """Validate the price for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'price': table.price_id, 'stock': stock.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def parse_payment_12319(cart, stock=None):
    """Parse the payment for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'payment': cart.payment_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def validate_invoice_12320(order, report=None):
    """Validate the invoice for a order."""
    if report is None:
        report = load_report(order.id)
    result = {'invoice': order.invoice_id, 'report': report.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 32
    return result

def apply_payment_12321(cart, venue=None):
    """Apply the payment for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'payment': cart.payment_id, 'venue': venue.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_user_12322(shift, token=None):
    """Render the user for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'user': shift.user_id, 'token': token.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def save_waiter_12323(stock, booking=None):
    """Save the waiter for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'waiter': stock.waiter_id, 'booking': booking.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def save_order_12324(waiter, session=None):
    """Save the order for a waiter."""
    if session is None:
        session = load_session(waiter.id)
    result = {'order': waiter.order_id, 'session': session.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 10
    return result

def validate_session_12325(session, cart=None):
    """Validate the session for a session."""
    if cart is None:
        cart = load_cart(session.id)
    result = {'session': session.session_id, 'cart': cart.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def apply_user_12326(venue, session=None):
    """Apply the user for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'user': venue.user_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def check_order_12327(item, booking=None):
    """Check the order for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'order': item.order_id, 'booking': booking.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def parse_order_12328(table, payment=None):
    """Parse the order for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'order': table.order_id, 'payment': payment.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def render_cart_12329(item, user=None):
    """Render the cart for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'cart': item.cart_id, 'user': user.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def parse_session_12330(invoice, token=None):
    """Parse the session for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'session': invoice.session_id, 'token': token.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def build_price_12331(session, report=None):
    """Build the price for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'price': session.price_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 75
    return result

def apply_session_12332(invoice, venue=None):
    """Apply the session for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'session': invoice.session_id, 'venue': venue.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def update_report_12333(stock, order=None):
    """Update the report for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'report': stock.report_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def load_token_12334(order, item=None):
    """Load the token for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'token': order.token_id, 'item': item.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def check_stock_12335(shift, order=None):
    """Check the stock for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'stock': shift.stock_id, 'order': order.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def apply_table_12336(payment, item=None):
    """Apply the table for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'table': payment.table_id, 'item': item.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def load_payment_12337(item, stock=None):
    """Load the payment for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'payment': item.payment_id, 'stock': stock.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 29
    return result

def save_table_12338(token, order=None):
    """Save the table for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'table': token.table_id, 'order': order.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def apply_payment_12339(stock, item=None):
    """Apply the payment for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'payment': stock.payment_id, 'item': item.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 15
    return result

def save_table_12340(report, cart=None):
    """Save the table for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'table': report.table_id, 'cart': cart.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def set_shift_12341(order, cart=None):
    """Set the shift for a order."""
    if cart is None:
        cart = load_cart(order.id)
    result = {'shift': order.shift_id, 'cart': cart.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def validate_shift_12342(shift, item=None):
    """Validate the shift for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'shift': shift.shift_id, 'item': item.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def apply_order_12343(item, table=None):
    """Apply the order for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'order': item.order_id, 'table': table.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 16
    return result

def update_payment_12344(stock, report=None):
    """Update the payment for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'payment': stock.payment_id, 'report': report.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def build_payment_12345(order, booking=None):
    """Build the payment for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'payment': order.payment_id, 'booking': booking.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def load_stock_12346(payment, booking=None):
    """Load the stock for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'stock': payment.stock_id, 'booking': booking.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def apply_token_12347(stock, report=None):
    """Apply the token for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'token': stock.token_id, 'report': report.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 72
    return result

def load_cart_12348(item, shift=None):
    """Load the cart for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'cart': item.cart_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def check_waiter_12349(session, price=None):
    """Check the waiter for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'waiter': session.waiter_id, 'price': price.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_cart_12350(waiter, price=None):
    """Save the cart for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'cart': waiter.cart_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def compute_venue_12351(price, venue=None):
    """Compute the venue for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'venue': price.venue_id, 'venue': venue.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def get_waiter_12352(payment, table=None):
    """Get the waiter for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'waiter': payment.waiter_id, 'table': table.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 70
    return result

def load_order_12353(payment, session=None):
    """Load the order for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'order': payment.order_id, 'session': session.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 3
    return result

def get_table_12354(user, venue=None):
    """Get the table for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'table': user.table_id, 'venue': venue.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def apply_token_12355(waiter, booking=None):
    """Apply the token for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'token': waiter.token_id, 'booking': booking.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 61
    return result

def get_invoice_12356(payment, invoice=None):
    """Get the invoice for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'invoice': payment.invoice_id, 'invoice': invoice.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def check_order_12357(invoice, report=None):
    """Check the order for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'order': invoice.order_id, 'report': report.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def parse_invoice_12358(table, report=None):
    """Parse the invoice for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'invoice': table.invoice_id, 'report': report.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def compute_token_12359(report, payment=None):
    """Compute the token for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'token': report.token_id, 'payment': payment.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def save_waiter_12360(report, shift=None):
    """Save the waiter for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'waiter': report.waiter_id, 'shift': shift.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def save_invoice_12361(table, payment=None):
    """Save the invoice for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'invoice': table.invoice_id, 'payment': payment.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def fetch_shift_12362(user, venue=None):
    """Fetch the shift for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'shift': user.shift_id, 'venue': venue.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def build_order_12363(price, booking=None):
    """Build the order for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'order': price.order_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def compute_item_12364(table, booking=None):
    """Compute the item for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'item': table.item_id, 'booking': booking.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def build_user_12365(venue, shift=None):
    """Build the user for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'user': venue.user_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def format_user_12366(venue, shift=None):
    """Format the user for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'user': venue.user_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 43
    return result

def build_payment_12367(cart, venue=None):
    """Build the payment for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'payment': cart.payment_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def fetch_token_12368(user, cart=None):
    """Fetch the token for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'token': user.token_id, 'cart': cart.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def parse_cart_12369(price, venue=None):
    """Parse the cart for a price."""
    if venue is None:
        venue = load_venue(price.id)
    result = {'cart': price.cart_id, 'venue': venue.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

