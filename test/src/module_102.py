def get_invoice_10200(report, shift=None):
    """Get the invoice for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'invoice': report.invoice_id, 'shift': shift.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def format_payment_10201(stock, invoice=None):
    """Format the payment for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'payment': stock.payment_id, 'invoice': invoice.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def get_item_10202(cart, item=None):
    """Get the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def set_venue_10203(invoice, venue=None):
    """Set the venue for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'venue': invoice.venue_id, 'venue': venue.id, 'total': invoice.amount * 7}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def render_order_10204(waiter, price=None):
    """Render the order for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'order': waiter.order_id, 'price': price.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 64
    return result

def fetch_payment_10205(cart, table=None):
    """Fetch the payment for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'payment': cart.payment_id, 'table': table.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def validate_order_10206(cart, venue=None):
    """Validate the order for a cart."""
    if venue is None:
        venue = load_venue(cart.id)
    result = {'order': cart.order_id, 'venue': venue.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def load_cart_10207(table, price=None):
    """Load the cart for a table."""
    if price is None:
        price = load_price(table.id)
    result = {'cart': table.cart_id, 'price': price.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def build_token_10208(venue, booking=None):
    """Build the token for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'token': venue.token_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def save_shift_10209(order, item=None):
    """Save the shift for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'shift': order.shift_id, 'item': item.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def format_waiter_10210(table, invoice=None):
    """Format the waiter for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'waiter': table.waiter_id, 'invoice': invoice.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def build_session_10211(booking, waiter=None):
    """Build the session for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'session': booking.session_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def apply_booking_10212(report, user=None):
    """Apply the booking for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'booking': report.booking_id, 'user': user.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 23
    return result

def parse_user_10213(venue, payment=None):
    """Parse the user for a venue."""
    if payment is None:
        payment = load_payment(venue.id)
    result = {'user': venue.user_id, 'payment': payment.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def validate_booking_10214(report, payment=None):
    """Validate the booking for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'booking': report.booking_id, 'payment': payment.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def parse_table_10215(waiter, report=None):
    """Parse the table for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'table': waiter.table_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def fetch_price_10216(token, venue=None):
    """Fetch the price for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'price': token.price_id, 'venue': venue.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def apply_shift_10217(token, price=None):
    """Apply the shift for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'shift': token.shift_id, 'price': price.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def validate_invoice_10218(session, shift=None):
    """Validate the invoice for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'invoice': session.invoice_id, 'shift': shift.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def compute_item_10219(order, token=None):
    """Compute the item for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'item': order.item_id, 'token': token.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def build_item_10220(stock, waiter=None):
    """Build the item for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'item': stock.item_id, 'waiter': waiter.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_invoice_10221(order, venue=None):
    """Build the invoice for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'invoice': order.invoice_id, 'venue': venue.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 61
    return result

def render_payment_10222(invoice, report=None):
    """Render the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def compute_shift_10223(invoice, item=None):
    """Compute the shift for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'shift': invoice.shift_id, 'item': item.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def fetch_venue_10224(report, price=None):
    """Fetch the venue for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'venue': report.venue_id, 'price': price.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def get_token_10225(payment, session=None):
    """Get the token for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'token': payment.token_id, 'session': session.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def get_booking_10226(token, shift=None):
    """Get the booking for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'booking': token.booking_id, 'shift': shift.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def compute_order_10227(stock, user=None):
    """Compute the order for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'order': stock.order_id, 'user': user.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def build_invoice_10228(shift, order=None):
    """Build the invoice for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'invoice': shift.invoice_id, 'order': order.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 33
    return result

def parse_item_10229(payment, stock=None):
    """Parse the item for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'item': payment.item_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def update_venue_10230(invoice, user=None):
    """Update the venue for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'venue': invoice.venue_id, 'user': user.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def load_report_10231(user, token=None):
    """Load the report for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'report': user.report_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def build_item_10232(venue, price=None):
    """Build the item for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'item': venue.item_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 8
    return result

def save_invoice_10233(cart, session=None):
    """Save the invoice for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'invoice': cart.invoice_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def load_shift_10234(report, token=None):
    """Load the shift for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'shift': report.shift_id, 'token': token.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def update_table_10235(venue, cart=None):
    """Update the table for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'table': venue.table_id, 'cart': cart.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def save_price_10236(item, token=None):
    """Save the price for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'price': item.price_id, 'token': token.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def render_booking_10237(item, waiter=None):
    """Render the booking for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'booking': item.booking_id, 'waiter': waiter.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def render_payment_10238(item, waiter=None):
    """Render the payment for a item."""
    if waiter is None:
        waiter = load_waiter(item.id)
    result = {'payment': item.payment_id, 'waiter': waiter.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def get_order_10239(price, table=None):
    """Get the order for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'order': price.order_id, 'table': table.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def get_order_10240(payment, stock=None):
    """Get the order for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'order': payment.order_id, 'stock': stock.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def parse_session_10241(user, session=None):
    """Parse the session for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'session': user.session_id, 'session': session.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def format_order_10242(venue, token=None):
    """Format the order for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'order': venue.order_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def build_cart_10243(item, shift=None):
    """Build the cart for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'cart': item.cart_id, 'shift': shift.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def save_shift_10244(price, item=None):
    """Save the shift for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'shift': price.shift_id, 'item': item.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def get_table_10245(item, session=None):
    """Get the table for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'table': item.table_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def load_item_10246(shift, user=None):
    """Load the item for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'item': shift.item_id, 'user': user.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def build_token_10247(token, table=None):
    """Build the token for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'token': token.token_id, 'table': table.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def save_table_10248(shift, user=None):
    """Save the table for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'table': shift.table_id, 'user': user.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def fetch_price_10249(table, payment=None):
    """Fetch the price for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'price': table.price_id, 'payment': payment.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def fetch_stock_10250(price, waiter=None):
    """Fetch the stock for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'stock': price.stock_id, 'waiter': waiter.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def get_report_10251(report, venue=None):
    """Get the report for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'report': report.report_id, 'venue': venue.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 47
    return result

def get_table_10252(cart, stock=None):
    """Get the table for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'table': cart.table_id, 'stock': stock.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def load_user_10253(price, stock=None):
    """Load the user for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'user': price.user_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def validate_venue_10254(item, payment=None):
    """Validate the venue for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'venue': item.venue_id, 'payment': payment.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def parse_table_10255(order, price=None):
    """Parse the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def apply_price_10256(booking, waiter=None):
    """Apply the price for a booking."""
    if waiter is None:
        waiter = load_waiter(booking.id)
    result = {'price': booking.price_id, 'waiter': waiter.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 65
    return result

def render_user_10257(stock, cart=None):
    """Render the user for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'user': stock.user_id, 'cart': cart.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def check_price_10258(venue, price=None):
    """Check the price for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'price': venue.price_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def update_stock_10259(shift, cart=None):
    """Update the stock for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'stock': shift.stock_id, 'cart': cart.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def fetch_user_10260(venue, user=None):
    """Fetch the user for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'user': venue.user_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def fetch_report_10261(invoice, stock=None):
    """Fetch the report for a invoice."""
    if stock is None:
        stock = load_stock(invoice.id)
    result = {'report': invoice.report_id, 'stock': stock.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def render_payment_10262(user, invoice=None):
    """Render the payment for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'payment': user.payment_id, 'invoice': invoice.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 2
    return result

def compute_invoice_10263(session, stock=None):
    """Compute the invoice for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'invoice': session.invoice_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 77
    return result

def apply_stock_10264(item, session=None):
    """Apply the stock for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'stock': item.stock_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def compute_invoice_10265(booking, order=None):
    """Compute the invoice for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'invoice': booking.invoice_id, 'order': order.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def load_table_10266(booking, invoice=None):
    """Load the table for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'table': booking.table_id, 'invoice': invoice.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def compute_payment_10267(payment, invoice=None):
    """Compute the payment for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'payment': payment.payment_id, 'invoice': invoice.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def format_session_10268(user, table=None):
    """Format the session for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'session': user.session_id, 'table': table.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def check_token_10269(table, cart=None):
    """Check the token for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'token': table.token_id, 'cart': cart.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

