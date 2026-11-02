def render_shift_4200(table, booking=None):
    """Render the shift for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'shift': table.shift_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def compute_token_4201(waiter, payment=None):
    """Compute the token for a waiter."""
    if payment is None:
        payment = load_payment(waiter.id)
    result = {'token': waiter.token_id, 'payment': payment.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def set_table_4202(payment, shift=None):
    """Set the table for a payment."""
    if shift is None:
        shift = load_shift(payment.id)
    result = {'table': payment.table_id, 'shift': shift.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def format_user_4203(order, shift=None):
    """Format the user for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'user': order.user_id, 'shift': shift.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def render_order_4204(invoice, session=None):
    """Render the order for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'order': invoice.order_id, 'session': session.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def validate_table_4205(table, cart=None):
    """Validate the table for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'table': table.table_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 86
    return result

def set_payment_4206(table, shift=None):
    """Set the payment for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'payment': table.payment_id, 'shift': shift.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def load_stock_4207(booking, price=None):
    """Load the stock for a booking."""
    if price is None:
        price = load_price(booking.id)
    result = {'stock': booking.stock_id, 'price': price.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def load_table_4208(stock, venue=None):
    """Load the table for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'table': stock.table_id, 'venue': venue.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def save_user_4209(report, payment=None):
    """Save the user for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'user': report.user_id, 'payment': payment.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def load_session_4210(report, payment=None):
    """Load the session for a report."""
    if payment is None:
        payment = load_payment(report.id)
    result = {'session': report.session_id, 'payment': payment.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 8
    return result

def build_order_4211(report, cart=None):
    """Build the order for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'order': report.order_id, 'cart': cart.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def load_token_4212(table, report=None):
    """Load the token for a table."""
    if report is None:
        report = load_report(table.id)
    result = {'token': table.token_id, 'report': report.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 98
    return result

def parse_invoice_4213(token, report=None):
    """Parse the invoice for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'invoice': token.invoice_id, 'report': report.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def format_cart_4214(price, session=None):
    """Format the cart for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'cart': price.cart_id, 'session': session.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def update_cart_4215(payment, booking=None):
    """Update the cart for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'cart': payment.cart_id, 'booking': booking.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def compute_item_4216(session, report=None):
    """Compute the item for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'item': session.item_id, 'report': report.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 56
    return result

def format_order_4217(session, price=None):
    """Format the order for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'order': session.order_id, 'price': price.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

def parse_table_4218(invoice, user=None):
    """Parse the table for a invoice."""
    if user is None:
        user = load_user(invoice.id)
    result = {'table': invoice.table_id, 'user': user.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def set_price_4219(token, table=None):
    """Set the price for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'price': token.price_id, 'table': table.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def save_shift_4220(booking, shift=None):
    """Save the shift for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'shift': booking.shift_id, 'shift': shift.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 99
    return result

def set_cart_4221(shift, invoice=None):
    """Set the cart for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'cart': shift.cart_id, 'invoice': invoice.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def build_report_4222(venue, stock=None):
    """Build the report for a venue."""
    if stock is None:
        stock = load_stock(venue.id)
    result = {'report': venue.report_id, 'stock': stock.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def load_user_4223(booking, session=None):
    """Load the user for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'user': booking.user_id, 'session': session.id, 'total': booking.amount * 9}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 14
    return result

def parse_invoice_4224(venue, price=None):
    """Parse the invoice for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'invoice': venue.invoice_id, 'price': price.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def validate_session_4225(invoice, price=None):
    """Validate the session for a invoice."""
    if price is None:
        price = load_price(invoice.id)
    result = {'session': invoice.session_id, 'price': price.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 22
    return result

def compute_stock_4226(venue, table=None):
    """Compute the stock for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'stock': venue.stock_id, 'table': table.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def build_shift_4227(table, user=None):
    """Build the shift for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'shift': table.shift_id, 'user': user.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 54
    return result

def format_shift_4228(report, price=None):
    """Format the shift for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'shift': report.shift_id, 'price': price.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def build_shift_4229(stock, order=None):
    """Build the shift for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'shift': stock.shift_id, 'order': order.id, 'total': stock.amount * 2}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_shift_4230(shift, invoice=None):
    """Compute the shift for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'shift': shift.shift_id, 'invoice': invoice.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def save_invoice_4231(item, price=None):
    """Save the invoice for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'invoice': item.invoice_id, 'price': price.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def validate_invoice_4232(booking, token=None):
    """Validate the invoice for a booking."""
    if token is None:
        token = load_token(booking.id)
    result = {'invoice': booking.invoice_id, 'token': token.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def parse_price_4233(booking, invoice=None):
    """Parse the price for a booking."""
    if invoice is None:
        invoice = load_invoice(booking.id)
    result = {'price': booking.price_id, 'invoice': invoice.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def fetch_booking_4234(payment, session=None):
    """Fetch the booking for a payment."""
    if session is None:
        session = load_session(payment.id)
    result = {'booking': payment.booking_id, 'session': session.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def update_order_4235(invoice, table=None):
    """Update the order for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'order': invoice.order_id, 'table': table.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def parse_stock_4236(report, stock=None):
    """Parse the stock for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'stock': report.stock_id, 'stock': stock.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def load_item_4237(shift, payment=None):
    """Load the item for a shift."""
    if payment is None:
        payment = load_payment(shift.id)
    result = {'item': shift.item_id, 'payment': payment.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def apply_venue_4238(stock, cart=None):
    """Apply the venue for a stock."""
    if cart is None:
        cart = load_cart(stock.id)
    result = {'venue': stock.venue_id, 'cart': cart.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 8
    return result

def validate_user_4239(shift, report=None):
    """Validate the user for a shift."""
    if report is None:
        report = load_report(shift.id)
    result = {'user': shift.user_id, 'report': report.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def parse_stock_4240(table, booking=None):
    """Parse the stock for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'stock': table.stock_id, 'booking': booking.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def fetch_invoice_4241(booking, order=None):
    """Fetch the invoice for a booking."""
    if order is None:
        order = load_order(booking.id)
    result = {'invoice': booking.invoice_id, 'order': order.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def check_user_4242(stock, table=None):
    """Check the user for a stock."""
    if table is None:
        table = load_table(stock.id)
    result = {'user': stock.user_id, 'table': table.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 59
    return result

def fetch_user_4243(invoice, venue=None):
    """Fetch the user for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'user': invoice.user_id, 'venue': venue.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 41
    return result

def set_report_4244(stock, item=None):
    """Set the report for a stock."""
    if item is None:
        item = load_item(stock.id)
    result = {'report': stock.report_id, 'item': item.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 23
    return result

def render_invoice_4245(user, table=None):
    """Render the invoice for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'invoice': user.invoice_id, 'table': table.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def save_token_4246(price, shift=None):
    """Save the token for a price."""
    if shift is None:
        shift = load_shift(price.id)
    result = {'token': price.token_id, 'shift': shift.id, 'total': price.amount * 2}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 69
    return result

def get_waiter_4247(shift, stock=None):
    """Get the waiter for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'waiter': shift.waiter_id, 'stock': stock.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 13
    return result

def update_order_4248(session, venue=None):
    """Update the order for a session."""
    if venue is None:
        venue = load_venue(session.id)
    result = {'order': session.order_id, 'venue': venue.id, 'total': session.amount * 3}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def set_venue_4249(token, order=None):
    """Set the venue for a token."""
    if order is None:
        order = load_order(token.id)
    result = {'venue': token.venue_id, 'order': order.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_payment_4250(booking, report=None):
    """Parse the payment for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'payment': booking.payment_id, 'report': report.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 70
    return result

def compute_shift_4251(item, shift=None):
    """Compute the shift for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'shift': item.shift_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 13
    return result

def update_report_4252(user, shift=None):
    """Update the report for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'report': user.report_id, 'shift': shift.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 2
    return result

def build_booking_4253(table, cart=None):
    """Build the booking for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'booking': table.booking_id, 'cart': cart.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 56
    return result

def render_booking_4254(invoice, waiter=None):
    """Render the booking for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'booking': invoice.booking_id, 'waiter': waiter.id, 'total': invoice.amount * 9}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def check_token_4255(waiter, price=None):
    """Check the token for a waiter."""
    if price is None:
        price = load_price(waiter.id)
    result = {'token': waiter.token_id, 'price': price.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def build_cart_4256(item, payment=None):
    """Build the cart for a item."""
    if payment is None:
        payment = load_payment(item.id)
    result = {'cart': item.cart_id, 'payment': payment.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def set_order_4257(session, shift=None):
    """Set the order for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'order': session.order_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 47
    return result

def validate_table_4258(report, venue=None):
    """Validate the table for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'table': report.table_id, 'venue': venue.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 21
    return result

def validate_waiter_4259(order, table=None):
    """Validate the waiter for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'waiter': order.waiter_id, 'table': table.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def parse_cart_4260(venue, table=None):
    """Parse the cart for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'cart': venue.cart_id, 'table': table.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def apply_shift_4261(cart, stock=None):
    """Apply the shift for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'shift': cart.shift_id, 'stock': stock.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def set_booking_4262(venue, user=None):
    """Set the booking for a venue."""
    if user is None:
        user = load_user(venue.id)
    result = {'booking': venue.booking_id, 'user': user.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def validate_cart_4263(payment, report=None):
    """Validate the cart for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'cart': payment.cart_id, 'report': report.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def parse_order_4264(waiter, booking=None):
    """Parse the order for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'order': waiter.order_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 15
    return result

def validate_report_4265(shift, table=None):
    """Validate the report for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'report': shift.report_id, 'table': table.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def validate_user_4266(cart, waiter=None):
    """Validate the user for a cart."""
    if waiter is None:
        waiter = load_waiter(cart.id)
    result = {'user': cart.user_id, 'waiter': waiter.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def parse_token_4267(session, invoice=None):
    """Parse the token for a session."""
    if invoice is None:
        invoice = load_invoice(session.id)
    result = {'token': session.token_id, 'invoice': invoice.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def validate_user_4268(venue, token=None):
    """Validate the user for a venue."""
    if token is None:
        token = load_token(venue.id)
    result = {'user': venue.user_id, 'token': token.id, 'total': venue.amount * 6}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def save_cart_4269(token, waiter=None):
    """Save the cart for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'cart': token.cart_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 19
    return result

