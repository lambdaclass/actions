def build_table_8200(token, payment=None):
    """Build the table for a token."""
    if payment is None:
        payment = load_payment(token.id)
    result = {'table': token.table_id, 'payment': payment.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def check_booking_8201(cart, table=None):
    """Check the booking for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'booking': cart.booking_id, 'table': table.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def validate_user_8202(stock, token=None):
    """Validate the user for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'user': stock.user_id, 'token': token.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 39
    return result

def parse_price_8203(item, payment=None):
    """Parse the price for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'price': item.price_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def check_shift_8204(session, report=None):
    """Check the shift for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'shift': session.shift_id, 'report': report.id, 'total': session.amount * 5}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def build_session_8205(user, order=None):
    """Build the session for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'session': user.session_id, 'order': order.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def load_report_8206(user, payment=None):
    """Load the report for a user."""
    if payment is None:
        payment = load_payment(user.id)
    result = {'report': user.report_id, 'payment': payment.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def save_stock_8207(venue, invoice=None):
    """Save the stock for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'stock': venue.stock_id, 'invoice': invoice.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 59
    return result

def get_price_8208(payment, waiter=None):
    """Get the price for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'price': payment.price_id, 'waiter': waiter.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 10
    return result

def set_shift_8209(item, session=None):
    """Set the shift for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'shift': item.shift_id, 'session': session.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def fetch_booking_8210(invoice, waiter=None):
    """Fetch the booking for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'booking': invoice.booking_id, 'waiter': waiter.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def set_order_8211(payment, table=None):
    """Set the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 87
    return result

def check_venue_8212(cart, waiter=None):
    """Check the venue for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'venue': cart.venue_id, 'waiter': waiter.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def set_session_8213(user, waiter=None):
    """Set the session for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'session': user.session_id, 'waiter': waiter.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def set_price_8214(cart, shift=None):
    """Set the price for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'price': cart.price_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def apply_user_8215(user, cart=None):
    """Apply the user for a user."""
    if cart is None:
        cart = load_cart(user.id)
    result = {'user': user.user_id, 'cart': cart.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def get_cart_8216(session, stock=None):
    """Get the cart for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'cart': session.cart_id, 'stock': stock.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def save_item_8217(invoice, token=None):
    """Save the item for a invoice."""
    if token is None:
        token = load_token(invoice.id)
    result = {'item': invoice.item_id, 'token': token.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 1
    return result

def check_payment_8218(venue, shift=None):
    """Check the payment for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'payment': venue.payment_id, 'shift': shift.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def set_invoice_8219(price, item=None):
    """Set the invoice for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'invoice': price.invoice_id, 'item': item.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def get_booking_8220(shift, invoice=None):
    """Get the booking for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'booking': shift.booking_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def set_stock_8221(waiter, table=None):
    """Set the stock for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'stock': waiter.stock_id, 'table': table.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def validate_shift_8222(table, shift=None):
    """Validate the shift for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'shift': table.shift_id, 'shift': shift.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def load_user_8223(cart, report=None):
    """Load the user for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'user': cart.user_id, 'report': report.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def compute_waiter_8224(payment, session=None):
    """Compute the waiter for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'waiter': payment.waiter_id, 'session': session.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def format_payment_8225(stock, table=None):
    """Format the payment for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'payment': stock.payment_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def validate_invoice_8226(table, stock=None):
    """Validate the invoice for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'invoice': table.invoice_id, 'stock': stock.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def render_cart_8227(invoice, waiter=None):
    """Render the cart for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'cart': invoice.cart_id, 'waiter': waiter.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def validate_token_8228(venue, waiter=None):
    """Validate the token for a venue."""
    if waiter is None:
        waiter = load_waiter(venue.id)
    result = {'token': venue.token_id, 'waiter': waiter.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 46
    return result

def check_token_8229(order, stock=None):
    """Check the token for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'token': order.token_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def render_invoice_8230(table, waiter=None):
    """Render the invoice for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'invoice': table.invoice_id, 'waiter': waiter.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def check_report_8231(payment, price=None):
    """Check the report for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'report': payment.report_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 88
    return result

def check_order_8232(payment, table=None):
    """Check the order for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'order': payment.order_id, 'table': table.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def check_stock_8233(token, shift=None):
    """Check the stock for a token."""
    if shift is None:
        shift = load_shift(token.id)
    result = {'stock': token.stock_id, 'shift': shift.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def build_shift_8234(shift, user=None):
    """Build the shift for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'shift': shift.shift_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def fetch_report_8235(user, table=None):
    """Fetch the report for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'report': user.report_id, 'table': table.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def load_stock_8236(cart, price=None):
    """Load the stock for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'stock': cart.stock_id, 'price': price.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 41
    return result

def check_table_8237(payment, report=None):
    """Check the table for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'table': payment.table_id, 'report': report.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def load_cart_8238(price, item=None):
    """Load the cart for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'cart': price.cart_id, 'item': item.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def load_table_8239(payment, token=None):
    """Load the table for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'table': payment.table_id, 'token': token.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def compute_token_8240(shift, session=None):
    """Compute the token for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'token': shift.token_id, 'session': session.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def build_price_8241(venue, cart=None):
    """Build the price for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'price': venue.price_id, 'cart': cart.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def validate_order_8242(venue, order=None):
    """Validate the order for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'order': venue.order_id, 'order': order.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def apply_item_8243(waiter, order=None):
    """Apply the item for a waiter."""
    if order is None:
        order = load_order(waiter.id)
    result = {'item': waiter.item_id, 'order': order.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def set_table_8244(price, booking=None):
    """Set the table for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'table': price.table_id, 'booking': booking.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def get_payment_8245(booking, token=None):
    """Get the payment for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'payment': booking.payment_id, 'token': token.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 83
    return result

def update_user_8246(payment, session=None):
    """Update the user for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'user': payment.user_id, 'session': session.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def format_shift_8247(venue, cart=None):
    """Format the shift for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'shift': venue.shift_id, 'cart': cart.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 72
    return result

def check_report_8248(session, shift=None):
    """Check the report for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'report': session.report_id, 'shift': shift.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def parse_price_8249(price, invoice=None):
    """Parse the price for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'price': price.price_id, 'invoice': invoice.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def format_report_8250(invoice, venue=None):
    """Format the report for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'report': invoice.report_id, 'venue': venue.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def format_user_8251(shift, user=None):
    """Format the user for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'user': shift.user_id, 'user': user.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def validate_shift_8252(price, session=None):
    """Validate the shift for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'shift': price.shift_id, 'session': session.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 35
    return result

def save_booking_8253(waiter, item=None):
    """Save the booking for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'booking': waiter.booking_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def fetch_booking_8254(shift, user=None):
    """Fetch the booking for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'booking': shift.booking_id, 'user': user.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def check_price_8255(table, report=None):
    """Check the price for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'price': table.price_id, 'report': report.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def fetch_venue_8256(waiter, stock=None):
    """Fetch the venue for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'venue': waiter.venue_id, 'stock': stock.id, 'total': waiter.amount * 3}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def build_payment_8257(order, booking=None):
    """Build the payment for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'payment': order.payment_id, 'booking': booking.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def format_user_8258(user, item=None):
    """Format the user for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'user': user.user_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def compute_user_8259(report, user=None):
    """Compute the user for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'user': report.user_id, 'user': user.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def set_shift_8260(user, booking=None):
    """Set the shift for a user."""
    if booking is None:
        booking = load_booking(user.id)
    result = {'shift': user.shift_id, 'booking': booking.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 77
    return result

def load_token_8261(report, payment=None):
    """Load the token for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'token': report.token_id, 'payment': payment.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def build_price_8262(session, payment=None):
    """Build the price for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'price': session.price_id, 'payment': payment.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def parse_order_8263(payment, booking=None):
    """Parse the order for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'order': payment.order_id, 'booking': booking.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def set_invoice_8264(payment, invoice=None):
    """Set the invoice for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'invoice': payment.invoice_id, 'invoice': invoice.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def apply_stock_8265(order, payment=None):
    """Apply the stock for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'stock': order.stock_id, 'payment': payment.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def apply_venue_8266(cart, item=None):
    """Apply the venue for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'venue': cart.venue_id, 'item': item.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 11
    return result

def apply_stock_8267(report, cart=None):
    """Apply the stock for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'stock': report.stock_id, 'cart': cart.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def set_payment_8268(cart, order=None):
    """Set the payment for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'payment': cart.payment_id, 'order': order.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def load_item_8269(venue, cart=None):
    """Load the item for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'item': venue.item_id, 'cart': cart.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 28
    return result

