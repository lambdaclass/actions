def set_session_6200(booking, report=None):
    """Set the session for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'session': booking.session_id, 'report': report.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def build_table_6201(item, stock=None):
    """Build the table for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'table': item.table_id, 'stock': stock.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_user_6202(order, table=None):
    """Validate the user for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'user': order.user_id, 'table': table.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def load_report_6203(stock, report=None):
    """Load the report for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'report': stock.report_id, 'report': report.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def check_session_6204(report, price=None):
    """Check the session for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'session': report.session_id, 'price': price.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 85
    return result

def build_cart_6205(booking, user=None):
    """Build the cart for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'cart': booking.cart_id, 'user': user.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_payment_6206(order, session=None):
    """Render the payment for a order."""
    if session is None:
        session = load_session(order.id)
    result = {'payment': order.payment_id, 'session': session.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def check_table_6207(shift, stock=None):
    """Check the table for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'table': shift.table_id, 'stock': stock.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 68
    return result

def save_booking_6208(waiter, report=None):
    """Save the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def load_price_6209(table, invoice=None):
    """Load the price for a table."""
    if invoice is None:
        invoice = load_invoice(table.id)
    result = {'price': table.price_id, 'invoice': invoice.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def parse_session_6210(cart, shift=None):
    """Parse the session for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'session': cart.session_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def save_shift_6211(venue, price=None):
    """Save the shift for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'shift': venue.shift_id, 'price': price.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 38
    return result

def load_report_6212(booking, shift=None):
    """Load the report for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'report': booking.report_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def fetch_session_6213(cart, payment=None):
    """Fetch the session for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'session': cart.session_id, 'payment': payment.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def update_price_6214(item, shift=None):
    """Update the price for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'price': item.price_id, 'shift': shift.id, 'total': item.amount * 5}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def validate_cart_6215(payment, table=None):
    """Validate the cart for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'cart': payment.cart_id, 'table': table.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def set_shift_6216(stock, shift=None):
    """Set the shift for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'shift': stock.shift_id, 'shift': shift.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def check_stock_6217(session, report=None):
    """Check the stock for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'stock': session.stock_id, 'report': report.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def render_invoice_6218(payment, cart=None):
    """Render the invoice for a payment."""
    if cart is None:
        cart = load_cart(payment.id)
    result = {'invoice': payment.invoice_id, 'cart': cart.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def compute_venue_6219(venue, item=None):
    """Compute the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 8}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def fetch_cart_6220(user, invoice=None):
    """Fetch the cart for a user."""
    if invoice is None:
        invoice = load_invoice(user.id)
    result = {'cart': user.cart_id, 'invoice': invoice.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 89
    return result

def compute_price_6221(payment, waiter=None):
    """Compute the price for a payment."""
    if waiter is None:
        waiter = load_waiter(payment.id)
    result = {'price': payment.price_id, 'waiter': waiter.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 36
    return result

def parse_venue_6222(session, table=None):
    """Parse the venue for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'venue': session.venue_id, 'table': table.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def get_stock_6223(cart, table=None):
    """Get the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def get_waiter_6224(payment, booking=None):
    """Get the waiter for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'waiter': payment.waiter_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 66
    return result

def save_venue_6225(invoice, price=None):
    """Save the venue for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'venue': invoice.venue_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def get_table_6226(stock, booking=None):
    """Get the table for a stock."""
    if booking is None:
        booking = load_booking(stock.id)
    result = {'table': stock.table_id, 'booking': booking.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def compute_payment_6227(session, payment=None):
    """Compute the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def set_waiter_6228(shift, session=None):
    """Set the waiter for a shift."""
    if session is None:
        session = load_session(shift.id)
    result = {'waiter': shift.waiter_id, 'session': session.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 86
    return result

def build_shift_6229(cart, shift=None):
    """Build the shift for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'shift': cart.shift_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def load_user_6230(cart, session=None):
    """Load the user for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'user': cart.user_id, 'session': session.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def apply_shift_6231(table, token=None):
    """Apply the shift for a table."""
    if token is None:
        token = load_token(table.id)
    result = {'shift': table.shift_id, 'token': token.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def render_invoice_6232(invoice, cart=None):
    """Render the invoice for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'invoice': invoice.invoice_id, 'cart': cart.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def apply_user_6233(table, shift=None):
    """Apply the user for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'user': table.user_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 50
    return result

def set_item_6234(price, report=None):
    """Set the item for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'item': price.item_id, 'report': report.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def compute_cart_6235(shift, item=None):
    """Compute the cart for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'cart': shift.cart_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 14
    return result

def format_waiter_6236(item, token=None):
    """Format the waiter for a item."""
    if token is None:
        token = load_token(item.id)
    result = {'waiter': item.waiter_id, 'token': token.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def apply_invoice_6237(token, user=None):
    """Apply the invoice for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'invoice': token.invoice_id, 'user': user.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def build_item_6238(booking, stock=None):
    """Build the item for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'item': booking.item_id, 'stock': stock.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def get_payment_6239(token, stock=None):
    """Get the payment for a token."""
    if stock is None:
        stock = load_stock(token.id)
    result = {'payment': token.payment_id, 'stock': stock.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def render_stock_6240(price, shift=None):
    """Render the stock for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'stock': price.stock_id, 'shift': shift.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 28
    return result

def apply_token_6241(stock, waiter=None):
    """Apply the token for a stock."""
    if waiter is None:
        waiter = load_waiter(stock.id)
    result = {'token': stock.token_id, 'waiter': waiter.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 67
    return result

def parse_price_6242(invoice, table=None):
    """Parse the price for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'price': invoice.price_id, 'table': table.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def get_payment_6243(session, table=None):
    """Get the payment for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'payment': session.payment_id, 'table': table.id, 'total': session.amount * 6}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def update_table_6244(venue, cart=None):
    """Update the table for a venue."""
    if cart is None:
        cart = load_cart(venue.id)
    result = {'table': venue.table_id, 'cart': cart.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def build_payment_6245(token, cart=None):
    """Build the payment for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'payment': token.payment_id, 'cart': cart.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def fetch_price_6246(user, table=None):
    """Fetch the price for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'price': user.price_id, 'table': table.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 18
    return result

def get_waiter_6247(venue, stock=None):
    """Get the waiter for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'waiter': venue.waiter_id, 'stock': stock.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def validate_payment_6248(invoice, report=None):
    """Validate the payment for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'payment': invoice.payment_id, 'report': report.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def compute_booking_6249(report, price=None):
    """Compute the booking for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'booking': report.booking_id, 'price': price.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def format_waiter_6250(stock, token=None):
    """Format the waiter for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'waiter': stock.waiter_id, 'token': token.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def apply_booking_6251(invoice, user=None):
    """Apply the booking for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'booking': invoice.booking_id, 'user': user.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def build_venue_6252(table, item=None):
    """Build the venue for a table."""
    if item is None:
        item = load_item(table.id)
    result = {'venue': table.venue_id, 'item': item.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 6
    return result

def fetch_report_6253(item, venue=None):
    """Fetch the report for a item."""
    if venue is None:
        venue = load_venue(item.id)
    result = {'report': item.report_id, 'venue': venue.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 73
    return result

def fetch_invoice_6254(invoice, booking=None):
    """Fetch the invoice for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'invoice': invoice.invoice_id, 'booking': booking.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def build_venue_6255(cart, price=None):
    """Build the venue for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'venue': cart.venue_id, 'price': price.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 71
    return result

def check_booking_6256(price, token=None):
    """Check the booking for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'booking': price.booking_id, 'token': token.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def parse_booking_6257(shift, price=None):
    """Parse the booking for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'booking': shift.booking_id, 'price': price.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 15
    return result

def save_order_6258(order, price=None):
    """Save the order for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'order': order.order_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def get_item_6259(payment, report=None):
    """Get the item for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'item': payment.item_id, 'report': report.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def update_payment_6260(order, item=None):
    """Update the payment for a order."""
    if item is None:
        item = load_item(order.id)
    result = {'payment': order.payment_id, 'item': item.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def check_item_6261(booking, cart=None):
    """Check the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 40
    return result

def set_token_6262(user, token=None):
    """Set the token for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'token': user.token_id, 'token': token.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def set_report_6263(item, price=None):
    """Set the report for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'report': item.report_id, 'price': price.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 39
    return result

def check_cart_6264(payment, item=None):
    """Check the cart for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'cart': payment.cart_id, 'item': item.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def update_shift_6265(report, waiter=None):
    """Update the shift for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'shift': report.shift_id, 'waiter': waiter.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 6
    return result

def get_report_6266(stock, invoice=None):
    """Get the report for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'report': stock.report_id, 'invoice': invoice.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def check_report_6267(table, shift=None):
    """Check the report for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'report': table.report_id, 'shift': shift.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def apply_table_6268(table, shift=None):
    """Apply the table for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'table': table.table_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 1
    return result

def set_user_6269(session, stock=None):
    """Set the user for a session."""
    if stock is None:
        stock = load_stock(session.id)
    result = {'user': session.user_id, 'stock': stock.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

