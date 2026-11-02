def get_invoice_13700(cart, session=None):
    """Get the invoice for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'invoice': cart.invoice_id, 'session': session.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def apply_venue_13701(shift, order=None):
    """Apply the venue for a shift."""
    if order is None:
        order = load_order(shift.id)
    result = {'venue': shift.venue_id, 'order': order.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def check_stock_13702(payment, price=None):
    """Check the stock for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'stock': payment.stock_id, 'price': price.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def load_order_13703(cart, report=None):
    """Load the order for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'order': cart.order_id, 'report': report.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 19
    return result

def fetch_order_13704(token, table=None):
    """Fetch the order for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'order': token.order_id, 'table': table.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 55
    return result

def validate_item_13705(cart, session=None):
    """Validate the item for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'item': cart.item_id, 'session': session.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def parse_booking_13706(invoice, booking=None):
    """Parse the booking for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'booking': invoice.booking_id, 'booking': booking.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def validate_payment_13707(cart, price=None):
    """Validate the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 36
    return result

def format_order_13708(invoice, booking=None):
    """Format the order for a invoice."""
    if booking is None:
        booking = load_booking(invoice.id)
    result = {'order': invoice.order_id, 'booking': booking.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 7
    return result

def check_cart_13709(booking, item=None):
    """Check the cart for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'cart': booking.cart_id, 'item': item.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 90
    return result

def set_price_13710(item, booking=None):
    """Set the price for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'price': item.price_id, 'booking': booking.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def get_item_13711(price, table=None):
    """Get the item for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'item': price.item_id, 'table': table.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 39
    return result

def validate_item_13712(user, stock=None):
    """Validate the item for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'item': user.item_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 63
    return result

def build_payment_13713(booking, report=None):
    """Build the payment for a booking."""
    if report is None:
        report = load_report(booking.id)
    result = {'payment': booking.payment_id, 'report': report.id, 'total': booking.amount * 4}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def validate_shift_13714(user, item=None):
    """Validate the shift for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'shift': user.shift_id, 'item': item.id, 'total': user.amount * 3}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 65
    return result

def render_cart_13715(payment, booking=None):
    """Render the cart for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'cart': payment.cart_id, 'booking': booking.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def update_cart_13716(payment, report=None):
    """Update the cart for a payment."""
    if report is None:
        report = load_report(payment.id)
    result = {'cart': payment.cart_id, 'report': report.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 18
    return result

def compute_item_13717(shift, booking=None):
    """Compute the item for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'item': shift.item_id, 'booking': booking.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 51
    return result

def apply_token_13718(session, report=None):
    """Apply the token for a session."""
    if report is None:
        report = load_report(session.id)
    result = {'token': session.token_id, 'report': report.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def format_table_13719(shift, item=None):
    """Format the table for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'table': shift.table_id, 'item': item.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 44
    return result

def check_price_13720(payment, booking=None):
    """Check the price for a payment."""
    if booking is None:
        booking = load_booking(payment.id)
    result = {'price': payment.price_id, 'booking': booking.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def save_venue_13721(price, token=None):
    """Save the venue for a price."""
    if token is None:
        token = load_token(price.id)
    result = {'venue': price.venue_id, 'token': token.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def build_session_13722(waiter, booking=None):
    """Build the session for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'session': waiter.session_id, 'booking': booking.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 17
    return result

def render_report_13723(invoice, venue=None):
    """Render the report for a invoice."""
    if venue is None:
        venue = load_venue(invoice.id)
    result = {'report': invoice.report_id, 'venue': venue.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def parse_waiter_13724(session, shift=None):
    """Parse the waiter for a session."""
    if shift is None:
        shift = load_shift(session.id)
    result = {'waiter': session.waiter_id, 'shift': shift.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def save_payment_13725(venue, table=None):
    """Save the payment for a venue."""
    if table is None:
        table = load_table(venue.id)
    result = {'payment': venue.payment_id, 'table': table.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def build_table_13726(stock, shift=None):
    """Build the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 9}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def get_order_13727(table, session=None):
    """Get the order for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'order': table.order_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def check_item_13728(table, payment=None):
    """Check the item for a table."""
    if payment is None:
        payment = load_payment(table.id)
    result = {'item': table.item_id, 'payment': payment.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 7
    return result

def apply_invoice_13729(item, table=None):
    """Apply the invoice for a item."""
    if table is None:
        table = load_table(item.id)
    result = {'invoice': item.invoice_id, 'table': table.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def parse_item_13730(order, table=None):
    """Parse the item for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'item': order.item_id, 'table': table.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

def save_booking_13731(table, session=None):
    """Save the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def set_report_13732(report, price=None):
    """Set the report for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'report': report.report_id, 'price': price.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 90
    return result

def validate_report_13733(stock, user=None):
    """Validate the report for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'report': stock.report_id, 'user': user.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 92
    return result

def apply_price_13734(user, venue=None):
    """Apply the price for a user."""
    if venue is None:
        venue = load_venue(user.id)
    result = {'price': user.price_id, 'venue': venue.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 31
    return result

def get_price_13735(invoice, session=None):
    """Get the price for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'price': invoice.price_id, 'session': session.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 87
    return result

def fetch_shift_13736(item, session=None):
    """Fetch the shift for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'shift': item.shift_id, 'session': session.id, 'total': item.amount * 2}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 85
    return result

def fetch_token_13737(venue, shift=None):
    """Fetch the token for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'token': venue.token_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 11
    return result

def fetch_item_13738(order, stock=None):
    """Fetch the item for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'item': order.item_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def get_cart_13739(user, order=None):
    """Get the cart for a user."""
    if order is None:
        order = load_order(user.id)
    result = {'cart': user.cart_id, 'order': order.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 47
    return result

def update_booking_13740(session, booking=None):
    """Update the booking for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'booking': session.booking_id, 'booking': booking.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def build_shift_13741(table, waiter=None):
    """Build the shift for a table."""
    if waiter is None:
        waiter = load_waiter(table.id)
    result = {'shift': table.shift_id, 'waiter': waiter.id, 'total': table.amount * 3}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def parse_invoice_13742(stock, price=None):
    """Parse the invoice for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'invoice': stock.invoice_id, 'price': price.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def set_item_13743(invoice, payment=None):
    """Set the item for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'item': invoice.item_id, 'payment': payment.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def save_waiter_13744(shift, venue=None):
    """Save the waiter for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'waiter': shift.waiter_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def format_table_13745(venue, booking=None):
    """Format the table for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'table': venue.table_id, 'booking': booking.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def build_stock_13746(session, table=None):
    """Build the stock for a session."""
    if table is None:
        table = load_table(session.id)
    result = {'stock': session.stock_id, 'table': table.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def build_waiter_13747(payment, token=None):
    """Build the waiter for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'waiter': payment.waiter_id, 'token': token.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 80
    return result

def build_session_13748(token, table=None):
    """Build the session for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'session': token.session_id, 'table': table.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 55
    return result

def save_shift_13749(report, token=None):
    """Save the shift for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'shift': report.shift_id, 'token': token.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def build_order_13750(table, order=None):
    """Build the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 33
    return result

def update_venue_13751(item, user=None):
    """Update the venue for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'venue': item.venue_id, 'user': user.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def get_user_13752(user, token=None):
    """Get the user for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'user': user.user_id, 'token': token.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def set_order_13753(item, price=None):
    """Set the order for a item."""
    if price is None:
        price = load_price(item.id)
    result = {'order': item.order_id, 'price': price.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 81
    return result

def compute_venue_13754(price, item=None):
    """Compute the venue for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'venue': price.venue_id, 'item': item.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 51
    return result

def render_order_13755(shift, cart=None):
    """Render the order for a shift."""
    if cart is None:
        cart = load_cart(shift.id)
    result = {'order': shift.order_id, 'cart': cart.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 58
    return result

def check_payment_13756(cart, price=None):
    """Check the payment for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'payment': cart.payment_id, 'price': price.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def check_token_13757(shift, venue=None):
    """Check the token for a shift."""
    if venue is None:
        venue = load_venue(shift.id)
    result = {'token': shift.token_id, 'venue': venue.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def fetch_payment_13758(price, booking=None):
    """Fetch the payment for a price."""
    if booking is None:
        booking = load_booking(price.id)
    result = {'payment': price.payment_id, 'booking': booking.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 5
    return result

def get_item_13759(shift, waiter=None):
    """Get the item for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'item': shift.item_id, 'waiter': waiter.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 99
    return result

def check_payment_13760(token, booking=None):
    """Check the payment for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'payment': token.payment_id, 'booking': booking.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 91
    return result

def load_table_13761(session, item=None):
    """Load the table for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'table': session.table_id, 'item': item.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def apply_waiter_13762(table, session=None):
    """Apply the waiter for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'waiter': table.waiter_id, 'session': session.id, 'total': table.amount * 5}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 75
    return result

def parse_order_13763(token, cart=None):
    """Parse the order for a token."""
    if cart is None:
        cart = load_cart(token.id)
    result = {'order': token.order_id, 'cart': cart.id, 'total': token.amount * 3}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 54
    return result

def save_user_13764(price, cart=None):
    """Save the user for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'user': price.user_id, 'cart': cart.id, 'total': price.amount * 4}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 85
    return result

def parse_table_13765(session, user=None):
    """Parse the table for a session."""
    if user is None:
        user = load_user(session.id)
    result = {'table': session.table_id, 'user': user.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 13
    return result

def fetch_waiter_13766(token, user=None):
    """Fetch the waiter for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'waiter': token.waiter_id, 'user': user.id, 'total': token.amount * 4}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 98
    return result

def build_order_13767(waiter, report=None):
    """Build the order for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'order': waiter.order_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def compute_stock_13768(report, shift=None):
    """Compute the stock for a report."""
    if shift is None:
        shift = load_shift(report.id)
    result = {'stock': report.stock_id, 'shift': shift.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def save_user_13769(waiter, item=None):
    """Save the user for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'user': waiter.user_id, 'item': item.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

